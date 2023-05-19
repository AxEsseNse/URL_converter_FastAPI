from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.feedback import SchemeFeedback, SchemeResponseFeedback
from service import Service


router_feedback = APIRouter()


@router_feedback.post('/', response_model=SchemeResponseFeedback)
async def func(request: SchemeFeedback, db: Session = Depends(Service.get_db)):
    user_msg = request.msg
    return Service.register_feedback(user_msg, db)
