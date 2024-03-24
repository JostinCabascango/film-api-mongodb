from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class FilmBase(BaseModel):
    """
    Base model for Film.
    """
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str


class FilmModel(FilmBase):
    """
    Film model. Inherits from FilmBase and adds an id and timestamps.
    """
    id: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class CreateFilmModel(FilmBase):
    """
    Model for creating a new Film. Inherits from FilmBase and adds timestamps.
    """
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class UpdateFilmModel(BaseModel):
    """
    Model for updating an existing Film. All attributes are optional.
    """
    title: Optional[str]
    director: Optional[str]
    year: Optional[int]
    genre: Optional[str]
    rating: Optional[float]
    country: Optional[str]
    updated_at: datetime = datetime.now()


class FilmsLimitResponse(BaseModel):
    """
    Response model for endpoints that return a limited number of Films.
    """
    row_count: int
    data: List[FilmModel]
