from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, update, table
from sqlalchemy.orm import Session

from utils.database import Base
import models


class User(Base):
    __tablename__ = "hawkeye_admin"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    salt = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_delete = Column(Integer, nullable=False)


def FindByName(user: User, db: Session):
    return db.query(User).filter(User.user_name == user.user_name).first()


def FindBySessionId(user: User, db: Session):
    return db.query(User).filter(User.id == user['id']).first()


def update(password: String,user: User, db: Session):
    db_user = db.query(User).filter(User.user_name == user['user_name']).first()
    if db_user:
        db_user.password = password
    db.commit()
    db.refresh(db_user)
    return db_user
