from pydantic import BaseModel


class SchemeURL(BaseModel):
    url: str

class SchemeFeedback(BaseModel):
    msg: str












class SchemeShortURL(BaseModel):
    short_url: str
    # Я хз как реализовать валидацию short TableModelURL. Потому что тут схема для json, а мне просто приходит переменная
    # типо vk.com/<peremennaya>

class URLBase(BaseModel):
    id: int
    short_url: str
    url: str
    date_creating: float
    count_use: int
    date_last_use: float

    class Config:
        orm_mode = True
