from fastapi import FastAPI
from handlers.users import user_router

app = FastAPI()
app.include_router(user_router)


@app.get("/")
def root() -> None:
    return {"msg": "Hello World"}
