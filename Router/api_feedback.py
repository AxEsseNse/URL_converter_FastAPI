from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.url import SchemeFeedback
from service import Service


router_feedback = APIRouter()


@router_feedback.post('/')
async def func(request: SchemeFeedback, db: Session = Depends(Service.get_db)):
    user_msg = request.dict()['msg']
    response = Service.register_feedback(user_msg, db)
    return response
