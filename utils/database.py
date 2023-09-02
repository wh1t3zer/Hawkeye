from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.file import read_config

config = read_config('mysql.yaml')
PORT = config['mysql']['port']
USERNAME = config['mysql']['username']
PASSWORD = config['mysql']['password']
TABLE_NAME = config['mysql']['table_name']
DATABASE_URL = "mysql+pymysql://{}:{}@localhost:{}/{}?charset=utf8".format(USERNAME, PASSWORD, PORT,TABLE_NAME)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
