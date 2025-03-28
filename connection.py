from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import BASE
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_PASSWORD = os.getenv("DB_PASSWORD")


uri: str = F'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/to-do-app'

engine = create_engine(uri)

BASE.metadata.create_all(bind = engine)

#session
session = sessionmaker(
    bind=engine,
    autoflush=True
)

db_session = session()

try:
    connection = engine.connect()
    connection.close()
    print('ping, connected')
except Exception as e:
    print(f'Error: {str(e)}')