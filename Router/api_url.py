from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.url import SchemeURL, SchemeResponseUrl
from service import Service
from error import DataBaseException


router_url = APIRouter()


@router_url.post('/', response_model=SchemeResponseUrl)
async def open_pole(request: SchemeURL, db: Session = Depends(Service.get_db)) -> dict[str, str]:
    user_url = request.url
    try:
        return Service.give_short_url(user_url, db)
    except Exception:
        raise DataBaseException('url')
