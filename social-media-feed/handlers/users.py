import os
from dotenv import load_dotenv
from datetime import timedelta
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from models.users import User
from services import users as user_service

load_dotenv()

user_router = APIRouter(prefix="/user", tags=["Users"])

TOKEN_EXPIRATION_IN_MINUTES = os.getenv("ACCESS_TOKEN_EXPIRATION_IN_MINUTES")


@user_router.post("/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = user_service.authenticate(
        username=form.username, password=form.password)
    expiration = timedelta(minutes=int(TOKEN_EXPIRATION_IN_MINUTES))

    access_token = user_service.create_token(user, expiration)

    return access_token


@user_router.get("/protected")
def protected_endpoint(user: User = Depends(user_service.manager)):
    return {"status": "logged"}
