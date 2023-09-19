from fastapi import FastAPI, Request
from views.cars_routes import car_router
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
app.include_router(car_router)


@app.route("/")
def home(request: Request) -> None:
    return templates.TemplateResponse("home.html", {"request": request, "title": "Project: Car Info"})
