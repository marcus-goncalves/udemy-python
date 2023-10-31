import os
import services.auth as auth
from dotenv import load_dotenv
from fastapi import HTTPException
from fastapi_login import LoginManager
from db import users
from models.users import UserDb

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

manager = LoginManager(secret=SECRET_KEY, token_url="/login", use_cookie=True)
manager.cookie_name = "auth"


@manager.user_loader()
def get_user(username: str):
    if username not in users.keys():
        raise HTTPException(
            status_code=401, detail="Invalid username or password")

    return UserDb(**users[username])


def authenticate(username: str, password: str):
    user = get_user(username)

    if not user:
        raise HTTPException(
            status_code=400, detail="Invalid username or password")

    if not auth.verify_password(plain_pwd=password, hashed_pwd=user.hashed_password):
        raise HTTPException(
            status_code=401, detail="Unauthorized")

    return user


def create_token(user: UserDb, expiration_in_minutes: int):
    access_token = manager.create_access_token(
        data={"sub": user.username},
        expires=expiration_in_minutes
    )
    return {"access_token": access_token}
