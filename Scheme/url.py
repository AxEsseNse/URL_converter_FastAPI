from pydantic import BaseModel


# Схемы для валидации


class URLBase(BaseModel):
    id: int
    short_url: str
    url: str
    date_creating: float
    count_use: int
    date_last_use: float

    class Config:
        orm_mode = True