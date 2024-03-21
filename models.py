from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class FilmModel(BaseModel):
    id: str
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CreateFilmModel(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class UpdateFilmModel(BaseModel):
    title: Optional[str]
    director: Optional[str]
    year: Optional[int]
    genre: Optional[str]
    rating: Optional[float]
    country: Optional[str]
    updated_at: datetime = datetime.now()


class FilmsLimitResponse(BaseModel):
    row_count: int
    data: List[FilmModel]
