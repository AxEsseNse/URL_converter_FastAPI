from fastapi import APIRouter

from Router.api_url import router_url
from Router.handlers import router_page


router = APIRouter()


router.include_router(router_page)
router.include_router(router_url, prefix='/api/url')
