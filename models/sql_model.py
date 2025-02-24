from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
import datetime

def get_timestamp():
    return datetime.datetime.now()

BASE = declarative_base()

#creating our model
class Todo(BASE):
    __tablename__: str = 'to_do'
    _id = Column(Integer, primary_key=True, autoincrement=True)
    todo = Column(String)
    timestamp = Column(DateTime, default=get_timestamp())

    def __init__(self, todo):
        self.todo = todo