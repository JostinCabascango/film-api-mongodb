from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from models import FilmModel, CreateFilmModel, UpdateFilmModel, FilmsLimitResponse
from services import films_service

router = APIRouter()


@router.get("/films/", response_model=List[FilmModel])
async def get_all_films():
    """Get all films"""
    try:
        films = await films_service.get_all_films()
        if not films:
            raise HTTPException(status_code=404, detail="No films found")
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/{film_id}", response_model=FilmModel)
async def get_single_film(film_id: str):
    """Get a single film by its ID"""
    try:
        film = await films_service.get_film(film_id)
        if not film:
            raise HTTPException(status_code=404, detail="Film not found")
        return film
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.post("/films/")
async def add_film(film: CreateFilmModel):
    """Create a new film"""
    try:
        new_film = await films_service.create_film(film)
        if not new_film:
            raise HTTPException(status_code=400, detail="Film could not be created")
        return JSONResponse(status_code=200, content={"success": True, "message": "Film created successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.put("/films/{film_id}")
async def update_single_film(film_id: str, film: UpdateFilmModel):
    """Update a film by its ID"""
    try:
        updated_film = await films_service.update_film(film_id, film)
        if not updated_film:
            raise HTTPException(status_code=400, detail="Film could not be updated")
        return JSONResponse(status_code=200, content={"success": True, "message": "Film updated successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.delete("/films/{film_id}")
async def remove_film(film_id: str):
    """Delete a film by its ID"""
    try:
        deleted_film = await films_service.delete_film(film_id)
        if not deleted_film:
            raise HTTPException(status_code=400, detail="Film could not be deleted")
        return JSONResponse(status_code=200, content={"success": True, "message": "Film deleted successfully"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/filter/", response_model=List[FilmModel])
async def get_films_by_genre(genre: Optional[str] = Query(None)):
    """
     Get films by genre
    :param genre:
    :return: films by genre
    """
    try:
        films = await films_service.get_films_by_genre(genre)
        if not films:
            raise HTTPException(status_code=404, detail="No films found")
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/sort/", response_model=List[FilmModel])
async def get_sorted_films(field: Optional[str] = Query(None), order: Optional[str] = Query(None)):
    """
    Get sorted films
    :param field:
    :param order:
    :return: sorted films
    """
    try:
        films = await films_service.get_sorted_films(field, order)
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})


@router.get("/films/limit/", response_model=FilmsLimitResponse)
async def get_limited_films(limit: Optional[int] = Query(None)):
    """
    Get limited films
    :param limit:
    :return: limited films
    """
    try:
        films = await films_service.get_limited_films(limit)
        return films
    except Exception as e:
        return JSONResponse(status_code=500, content={"success": False, "message": str(e)})
