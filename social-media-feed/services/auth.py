from passlib.context import CryptContext

pwd_ctx: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hashed_password(plain_pwd) -> str:
    return pwd_ctx.hash(plain_pwd)


def verify_password(plain_pwd, hashed_pwd) -> bool:
    return pwd_ctx.verify(plain_pwd, hashed_pwd)
