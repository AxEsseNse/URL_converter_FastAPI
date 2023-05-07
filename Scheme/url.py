from pydantic import BaseModel


# Схемы для валидации

class Url(BaseModel):
    url: str


class SchemeShortURL(BaseModel):
    short_url: str
    # Я хз как реализовать валидацию short url. Потому что тут схема для json, а мне просто приходит переменная
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
