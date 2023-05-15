import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Router.main import router
from DataBase import SessionLocal

from starlette.requests import Request
from starlette.responses import Response


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


if __name__ == '__main__':
    uvicorn.run(app, port=5000)
