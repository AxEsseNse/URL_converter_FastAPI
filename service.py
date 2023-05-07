from starlette.requests import Request
from DataBase import engine
from DBModel.table import url
from DBModel.model import ModelURL
from shorter import create_short_url


BASE_URL = 'http://127.0.0.1:5000/'


class Service:
    @staticmethod
    def get_db(request: Request):
        return request.state.db

    @staticmethod
    def check_url(user_url):
        conn = engine.connect()
        query_select = url.select().where(url.columns.url == user_url)
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
