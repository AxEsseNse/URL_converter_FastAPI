from pydantic import BaseModel


class SchemeFeedback(BaseModel):
    msg: str


class SchemeResponseFeedback(BaseModel):
    data: str
    date: str
    code: bool
