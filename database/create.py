from .core import engine, Session
from .models import User
import utils


def create_user(user_id: int, name: str, data: str) -> User:
    with Session(autoflush=False, bind=engine) as db:
        user = User(id=user_id, name=name, data=data)
        db.add(user)
        db.commit()
        return user


def add_data_db(user_id:int(), pn:int(), data:str()):
    with Session(autoflush=False, bind=engine) as db:
        user = db.get(User, user_id)
        print(user.data)
        db.commit()
        return user