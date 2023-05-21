from DataBase import SessionLocal
from DBModel.model import ModelURL
from datetime import datetime


def get_time_now() -> float:
    return datetime.timestamp(datetime.utcnow())


def calculate_condition() -> float:
    return get_time_now() - 604800


def delete_old_data():
    condition = calculate_condition()
    session = SessionLocal()
    session.query(ModelURL).filter(ModelURL.date_last_use < condition).delete()
    session.commit()
    session.close()


if __name__ == '__main__':
    delete_old_data()
