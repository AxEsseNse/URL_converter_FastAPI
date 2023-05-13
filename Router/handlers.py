from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from service import Service


router_page = APIRouter()
templates = Jinja2Templates(directory='templates')


@router_page.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router_page.get('/{variable}', response_class=HTMLResponse)
async def link_url(request: Request, variable: str):
    response = Service.give_url(variable)
    if response['data'] is None:
        return templates.TemplateResponse('wrong.html', {'request': request, 'data': response})
    else:
        return templates.TemplateResponse('redirect.html', {'request': request, 'data': response})
