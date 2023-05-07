from starlette.requests import Request
from DataBase import engine
from DBModel.table import TableModelURL, TableModelFeedback
from DBModel.model import ModelURL, ModelFeedback
from shorter import create_short_url
from datetime import datetime


BASE_URL = 'http://127.0.0.1:5000/'


class Service:
    @staticmethod
    def get_db(request: Request):
        return request.state.db

    @staticmethod
    def check_url(user_url):
        conn = engine.connect()
        query_select = TableModelURL.select().where(TableModelURL.columns.url == user_url)
        database_request = conn.execute(query_select)
        database_response = database_request.fetchone()
        return database_response

    @staticmethod
    def give_short_url(user_url, db):
        database_data = Service.check_url(user_url)
        if database_data is None:
            short_url = create_short_url()
            new_data = ModelURL(url=user_url, short_url=short_url)
            db.add(new_data)
            db.commit()
            return {'data': f'{BASE_URL}{short_url}', 'comment': 'Your URL added to DataBase. Short URL returned.'}
        else:
            return {'data': f'{BASE_URL}{database_data.short_url}',
                    'comment': 'There is this URL in DataBase already. Returned corresponding short URL from DataBase.'}


    @staticmethod
    def check_feedback(user_msg):
        conn = engine.connect()
        query_select = TableModelFeedback.select().where(TableModelFeedback.columns.msg == user_msg)
        database_request = conn.execute(query_select)
        database_response = database_request.fetchone()
        return database_response

    @staticmethod
    def register_feedback(user_msg, db):
        database_data = Service.check_feedback(user_msg)
        if database_data is None:
            new_data = ModelFeedback(msg=user_msg)
            db.add(new_data)
            db.commit()
            date = f"Дата Вашего обращения: {datetime.utcnow().strftime('%d.%m.%Y')}"
            return {'data': 'Ваще обращение успешно зарегистрировано.', 'date': date, 'code': True}
        else:
            date = f"Дата обращения: {datetime.fromtimestamp(database_data.date).strftime('%d.%m.%Y')}"
            return {'data': 'Обращение с идентичным содержимым уже зарегистрировано.', 'date': date, 'code': False}
