from DataBase import ModelORM
from sqlalchemy import Column, Integer, String, Float
from datetime import datetime


class ModelURL(ModelORM):
    __tablename__ = 'FA_url'
    id = Column(Integer, primary_key=True, unique=True)
    short_url = Column(String, unique=True)
    url = Column(String, unique=True)
    date_creating = Column(Float, default=datetime.timestamp(datetime.utcnow()))
    count_use = Column(Integer, default=1)
    date_last_use = Column(Float, default=datetime.timestamp(datetime.utcnow()))


class ModelFeedback(ModelORM):
    __tablename__ = 'FA_feedback'
    id = Column(Integer, primary_key=True, unique=True)
    msg = Column(String, unique=True)
    date = Column(Float, default=datetime.timestamp(datetime.utcnow()))
