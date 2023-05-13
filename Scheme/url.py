from pydantic import BaseModel


class SchemeURL(BaseModel):
    url: str

class SchemeFeedback(BaseModel):
    msg: str


# Вот этим пока хз как пользоваться
class URLBase(BaseModel):
    id: int
    short_url: str
    url: str
    date_creating: float
    count_use: int
    date_last_use: float

    class Config:
        orm_mode = True
