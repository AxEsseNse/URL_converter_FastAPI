import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Router.main import router
from DataBase import SessionLocal

from starlette.requests import Request
from starlette.responses import Response

from fastapi.responses import PlainTextResponse, JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException

app = FastAPI()
app.mount('/static', StaticFiles(directory='static', html=True), name='static')
app.include_router(router)


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
            content={'data': 'Отправлены некорректные данные', 'date': 'Ошибка', 'code': False}
        )


if __name__ == '__main__':
    uvicorn.run(app, port=5000)
