from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import Session

from utils.database import Base


class User(Base):
    __tablename__ = "hawkeye_admin"
    id = Column(Integer, primary_key=True, index=True, nullable=False)  # 自增主键
    user_name = Column(String, unique=True, nullable=False)  # 管理员用户名
    salt = Column(String, nullable=False)  # 盐
    password = Column(String, nullable=False)  # 密码
    create_at = Column(DateTime, default=datetime.now(), nullable=False)  # 更新时间
    update_at = Column(DateTime, default=datetime.now(), nullable=False)  # 创建时间
    is_delete = Column(Integer, nullable=False)  # 是否删除

# 通过用户名查找且禁用状态为否
def FindByName(user: User, db: Session):
    return db.query(User).filter(User.user_name == user.user_name and User.is_delete == '0').first()


def FindBySessionId(user: User, db: Session):
    return db.query(User).filter(User.id == user['id']).first()


def update(password: String, user: User, db: Session):
    db_user = db.query(User).filter(User.user_name == user['user_name']).first()
    if db_user:
        db_user.password = password
    db.commit()
    db.refresh(db_user)
    return db_user
