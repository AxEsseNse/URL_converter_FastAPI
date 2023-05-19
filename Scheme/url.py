from pydantic import BaseModel, AnyHttpUrl


class SchemeURL(BaseModel):
    url: AnyHttpUrl


class SchemeResponseUrl(BaseModel):
    data: str
    comment: str
