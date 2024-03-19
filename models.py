from datetime import datetime

from pydantic import BaseModel


class FilmModel(BaseModel):
    title: str
    director: str
    year: int
    genre: str
    rating: float
    country: str
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
