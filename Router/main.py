from fastapi import APIRouter
from Router.handlers import router_page
from Router.api_url import router_url
from Router.api_feedback import router_feedback


router = APIRouter()


router.include_router(router_page)
router.include_router(router_url, prefix='/api/url')
router.include_router(router_feedback, prefix='/api/feedback')
