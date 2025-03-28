from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_model import BASE
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_password = os.getenv("DB_PASSWORD")


uri: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/to-do-app'

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