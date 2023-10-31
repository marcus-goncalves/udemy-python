from pydantic import BaseModel


class Notifications(BaseModel):
    author: str
    description: str


class User(BaseModel):
    name: str
    username: str
    email: str
    birthday: str
    friends: list[str]
    notifications: list[Notifications]


class UserDb(User):
    hashed_password: str
