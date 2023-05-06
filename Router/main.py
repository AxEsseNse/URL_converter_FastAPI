from fastapi import APIRouter
from Router.url import router_url


router = APIRouter()


router.include_router(router_url, prefix='/url')
