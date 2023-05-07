from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.url import Url
from service import Service


router_url = APIRouter()
BASE_URL = 'http://127.0.0.1:5000/'


@router_url.post('/')
def func(request: Url, db: Session = Depends(Service.get_db)):
    user_url = request.dict()['url']
    response = Service.give_short_url(user_url, db)
    return response
# @router_url.get('/', response_model=URLBase)
# def url_get(db: Session = Depends(get_db)):
#     return services.get_url(db)
