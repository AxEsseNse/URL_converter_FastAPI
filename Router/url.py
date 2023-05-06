from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import get_db
# Вынести логику в сервис и импортировать типо как ниже
# from service import url_add, url_get
# Ниже импортируем схемы, которым должны соответствовать принимаемые данные и отправляемые данные
from Scheme.url import URLBase


router_url = APIRouter()


@router_url.get('/', response_model=URLBase)
def url_get(db: Session = Depends(get_db)):
    return services.get_url(db)


@router_url.post('/')
def url_create(url: URLBase, db: Session = Depends(get_db)):
    return services.create_url(db, url)
