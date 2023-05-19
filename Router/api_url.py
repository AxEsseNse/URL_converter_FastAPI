from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.url import SchemeURL, SchemeResponseUrl
from service import Service


router_url = APIRouter()


@router_url.post('/', response_model=SchemeResponseUrl)
async def func(request: SchemeURL, db: Session = Depends(Service.get_db)):
    user_url = request.url
    return Service.give_short_url(user_url, db)
