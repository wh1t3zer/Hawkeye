from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from utils.database import Base


class User(Base):
    __tablename__ = "hawkeye_admin"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    user_name = Column(String, unique=True, nullable=False)
    salt = Column(String, nullable=False)
    password = Column(String, nullable=False)
    create_at = Column(DateTime, default=datetime.now(), nullable=False)
    update_at = Column(DateTime, default=datetime.now(), nullable=False)
    is_delete = Column(Integer, nullable=False)




