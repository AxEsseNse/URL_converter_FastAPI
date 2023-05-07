from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates


router_page = APIRouter()
templates = Jinja2Templates(directory='templates')


@router_page.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
