from fastapi import FastAPI
from Router.main import router
from starlette.requests import Request
from starlette.responses import Response
from DataBase import SessionLocal


app = FastAPI()
app.include_router(router)


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Server is not available', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response
