from starlette.requests import Request
from starlette.templating import Jinja2Templates
from DBModel.model import ModelURL, ModelFeedback
from shorter import create_short_url
from datetime import datetime

from sqlalchemy.orm import Session, sessionmaker
from pydantic import AnyHttpUrl


BASE_URL = 'http://127.0.0.1:5000/'
templates = Jinja2Templates(directory='templates')


class Service:
    @staticmethod
    def get_db(request: Request) -> sessionmaker:
        return request.state.db

    @staticmethod
    def check_url(user_url: AnyHttpUrl, db: Session) -> ModelURL | None:
        return db.query(ModelURL).filter_by(url=user_url).first()

    @staticmethod
    def check_short_url(user_short_url: str, db: Session) -> ModelURL | None:
        return db.query(ModelURL).filter_by(short_url=user_short_url).first()

    @staticmethod
    def update_url_data(data: ModelURL, db: Session) -> int:
        data.count_use += 1
        data.date_last_use = datetime.timestamp(datetime.utcnow())
        db.commit()
        return data.count_use

    @classmethod
    def give_short_url(cls, user_url: AnyHttpUrl, db: Session) -> dict[str, str]:
        database_data = cls.check_url(user_url, db)
        if database_data is None:
            short_url = create_short_url()
            new_data = ModelURL(url=user_url, short_url=short_url)
            db.add(new_data)
            db.commit()
            return {'data': f'{BASE_URL}{short_url}', 'comment': 'Your URL added to DataBase. Short URL returned.'}
        else:
            cls.update_url_data(database_data, db)
            return {'data': f'{BASE_URL}{database_data.short_url}',
                    'comment': 'There is this URL in DataBase already. Returned corresponding short URL from DataBase.'}

    @classmethod
    def give_url(cls, user_short_url: str, db: Session) -> dict[str, str | bool]:
        database_data = cls.check_short_url(user_short_url, db)
        if database_data is None:
            return {'data': None, 'comment': 'There is not this short URL in DataBase'}
        else:
            return {'data': database_data.url, 'comment': 'URL executed from DataBase'}

    @staticmethod
    def check_feedback(user_msg: str, db: Session) -> ModelFeedback | None:
        return db.query(ModelFeedback).filter_by(msg=user_msg).first()

    @classmethod
    def register_feedback(cls, user_msg: str, db: Session) -> dict[str, str | bool]:
        database_data = cls.check_feedback(user_msg, db)
        if database_data is None:
            new_data = ModelFeedback(msg=user_msg)
            db.add(new_data)
            db.commit()
            date = f"Дата Вашего обращения: {datetime.utcnow().strftime('%d.%m.%Y')}"
            return {'data': 'Ваше обращение успешно зарегистрировано.', 'date': date, 'code': True}
        else:
            date = f"Дата обращения: {datetime.fromtimestamp(database_data.date).strftime('%d.%m.%Y')}"
            return {'data': 'Обращение с идентичным содержимым уже зарегистрировано.', 'date': date, 'code': False}
