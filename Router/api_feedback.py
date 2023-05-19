from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Scheme.feedback import SchemeFeedback, SchemeResponseFeedback
from service import Service
from error import DataBaseException


router_feedback = APIRouter()


@router_feedback.post('/', response_model=SchemeResponseFeedback)
async def func(request: SchemeFeedback, db: Session = Depends(Service.get_db)) -> dict[str, str | bool]:
    user_msg = request.msg
    try:
        return Service.register_feedback(user_msg, db)
    except Exception:
        raise DataBaseException('feedback')
