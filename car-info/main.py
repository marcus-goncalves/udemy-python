from fastapi import FastAPI
from views.cars_routes import car_router

app = FastAPI()
app.include_router(car_router)

@app.route("/")
def home() -> None:
    return {"msg": "Hello World!"}
