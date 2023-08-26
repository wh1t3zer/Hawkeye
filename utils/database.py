from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USERNAME = 'root'
PASSWORD = '123456'
PORT = 3306
DATABASE_URL = "mysql+pymysql://{}:{}@localhost:{}/Hawkeye?charset=utf8".format(USERNAME,PASSWORD,PORT)

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
