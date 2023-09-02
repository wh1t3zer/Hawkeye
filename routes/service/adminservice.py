import models.user
from sqlalchemy.orm import Session

from models.user import User

def Find(db: Session, user:User):
    db_user = db.query(models.user.User).filter(models.user.User.user_name == user.user_name).first()

