from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.url import SchemeURL
from service import Service
from validators import url as url_validator


router_url = APIRouter()


# Жек, вот тут я так понял проферы не через валидацию (библиотеку) делают, а через саму схему, а в ней регулярку, да?
@router_url.post('/')
async def func(request: SchemeURL, db: Session = Depends(Service.get_db)):
    user_url = request.dict()['url']
    if url_validator(user_url):
        # Тут хотел поставить await. Типо соединение с бд же, операция требующая времени. А она не дает. await ваще нужен?
        response = Service.give_short_url(user_url, db)
    else:
        response = {'data': 'incorrect url', 'comment': 'URL incorrect'}
    return response
