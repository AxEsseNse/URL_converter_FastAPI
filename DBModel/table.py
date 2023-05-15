from sqlalchemy import MetaData, Table, Column, Integer, Float, String
from datetime import datetime


metadata = MetaData()


# Таблицы удалить ( переписать в миграцию алембика)

TableModelURL = Table('FA_url', metadata,
                      Column('id', Integer(), primary_key=True),
                      Column('short_url', String(5), unique=True),
                      Column('url', String(), unique=True),
                      Column('date_creating', Float(), default=datetime.timestamp(datetime.utcnow())),
                      Column('count_use', Integer(), default=1),
                      Column('date_last_use', Float(), default=datetime.timestamp(datetime.utcnow()))
                      )

TableModelFeedback = Table('FA_feedback', metadata,
                           Column('id', Integer(), primary_key=True),
                           Column('msg', String(250), unique=True),
                           Column('date', Float(), default=datetime.timestamp(datetime.utcnow()))
                           )
