from fastapi import APIRouter, Query, Path, HTTPException, status
from fastapi.encoders import jsonable_encoder
from schemas.car import Car, CarCreate, CarUpdate
from database.cars import cars as cars_data

max_items_per_request: int = 50
min_car_id_request: int = 1

car_router = APIRouter(prefix="/cars", tags=["Cars"])


@car_router.get("", response_model=list[dict[str, Car]], status_code=status.HTTP_200_OK)
def get_cars(items: int | None = Query("5", lt=max_items_per_request)) -> list:
    response: list = []
    for id, car in list(cars_data.items())[:items]:
        item: dict = {}
        item[id] = car
        response.append(item)

    return response


@car_router.get("/{car_id}", response_model=Car, status_code=status.HTTP_200_OK)
def get_car_by_id(car_id: int = Path(..., ge=min_car_id_request)) -> Car:
    car = cars_data.get(car_id)
    if not car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return car


@car_router.post("", response_model=CarCreate, status_code=status.HTTP_201_CREATED)
def create_car(car: Car) -> None:
    car_id: int = len(cars_data.values()) + 1
    cars_data[car_id] = car

    return CarCreate(car_id=car_id)


@car_router.put("/{car_id}", response_model=Car, status_code=status.HTTP_202_ACCEPTED)
def update_car(car_id: int, car: CarUpdate) -> Car:
    old_car: dict = cars_data.get(car_id)
    if not old_car:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    old_car = Car(**dict(old_car))
    new_car: dict = car.dict(exclude_unset=True)
    new_car = old_car.copy(update=new_car)
    cars_data[car_id] = jsonable_encoder(new_car)

    print(cars_data)
    return new_car


@car_router.delete("/{car_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_car(car_id: int) -> None:
    if not cars_data.get(car_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    del cars_data[id]
    return
