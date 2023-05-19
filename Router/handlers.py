from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from service import Service
from sqlalchemy.orm import Session
from error import DataBaseException


router_page = APIRouter()
templates = Jinja2Templates(directory='templates')


@router_page.get('/', response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router_page.get('/{variable}', response_class=HTMLResponse)
async def link_url(request: Request, variable: str, db: Session = Depends(Service.get_db)):
    try:
        response = Service.give_url(variable, db)
        if response['data'] is None:
            return templates.TemplateResponse('wrong.html', {'request': request, 'data': response}, status_code=404)
        else:
            return templates.TemplateResponse('redirect.html', {'request': request, 'data': response})
    except Exception:
        raise DataBaseException('short_url')
