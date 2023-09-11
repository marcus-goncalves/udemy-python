from pydantic import BaseModel, Field
from typing import Optional

min_year: int = 1970
max_year: int = 2022


class Car(BaseModel):
    company: str
    model: str
    year: int = Field(..., gt=min_year, le=max_year)
    price: float
    autonomous: bool
    sold: list[str]
    engine: str | None = "V4"


class CarCreate(BaseModel):
    car_id: int


class CarUpdate(BaseModel):
    company: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(gt=min_year, le=max_year,)
    price: Optional[float]
    autonomous: Optional[bool]
    sold: Optional[list[str]]
    engine: Optional[str] = "V4"
