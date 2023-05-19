import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Router.main import router
from DataBase import SessionLocal

from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.responses import Response
from fastapi.responses import JSONResponse

from fastapi.exceptions import RequestValidationError
from error import DataBaseException


app = FastAPI()
app.mount('/static', StaticFiles(directory='static', html=True), name='static')
app.include_router(router)
templates = Jinja2Templates(directory='templates')


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal Server Error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.exception_handler(RequestValidationError)
async def wrong_url_format(request: Request, exc: RequestValidationError):
    body = exc.body
    if 'url' in body:
        return JSONResponse(
            status_code=400,
            content={'data': 'incorrect url', 'comment': 'URL incorrect'}
        )
    elif 'msg' in body:
        return JSONResponse(
            status_code=400,
            content={'data': 'Отправлены некорректные данные', 'date': '', 'code': False}
        )


@app.exception_handler(DataBaseException)
def database_error(request: Request, exc: DataBaseException):
    if exc.api == 'url':
        return JSONResponse(
            status_code=500,
            content={'data': 'Sorry. DB Server error', 'comment': 'DataBase Error'}
        )
    elif exc.api == 'feedback':
        return JSONResponse(
            status_code=500,
            content={'data': 'DB Server error', 'date': '', 'code': False}
        )
    elif exc.api == 'short_url':
        return templates.TemplateResponse(name='error.html',
                                          context={'request': request,
                                                   'data': {'comment': 'Error with Server DataBase'}},
                                          status_code=500)


if __name__ == '__main__':
    uvicorn.run(app, port=5000)
