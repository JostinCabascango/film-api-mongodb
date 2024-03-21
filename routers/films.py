from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from models import FilmModel, CreateFilmModel, UpdateFilmModel, FilmsLimitResponse
from services import films_service

router = APIRouter()


@router.get("/films/", response_model=List[FilmModel])
async def read_films():
    try:
        films = await films_service.read_films()
        if films:
            return films
        else:
            raise HTTPException(status_code=404, detail="No films found")
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/{id}", response_model=FilmModel)
async def get_film(id: str):
    try:
        film = await films_service.get_film(id)
        if film:
            return film
        else:
            raise HTTPException(status_code=404, detail="Film not found")
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.post("/films/")
async def create_film(film: CreateFilmModel):
    try:
        new_film = await films_service.create_film(film)
        if new_film:
            return JSONResponse(status_code=200, content={"success": True, "message": "Film created successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.put("/films/{id}")
async def update_film(id: str, film: UpdateFilmModel):
    try:
        updated_film = await films_service.update_film(id, film)
        if updated_film:
            return JSONResponse(status_code=200, content={"success": True, "message": "Film updated successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.delete("/films/{id}")
async def delete_film(id: str):
    try:
        deleted_film = await films_service.delete_film(id)
        if deleted_film:
            return JSONResponse(status_code=200, content={"success": True, "message": "Film deleted successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/filter/", response_model=List[FilmModel])
async def get_films_by_genre(genre: Optional[str] = Query(None)):
    try:
        films = await films_service.get_films_by_genre(genre)
        if films:
            return films
        else:
            raise HTTPException(status_code=404, detail="No films found")
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/sort/", response_model=List[FilmModel])
async def read_films_sorted(field: Optional[str] = Query(None, alias="field"),
                            order: Optional[str] = Query(None, alias="order")):
    try:
        films = await films_service.read_films_sorted(field, order)
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/limit/", response_model=FilmsLimitResponse)
async def read_films_limit(limit: Optional[int] = Query(None, alias="limit")):
    try:
        films = await films_service.read_films_limit(limit)
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})
