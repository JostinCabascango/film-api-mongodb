from fastapi import APIRouter

from services import films_service

router = APIRouter()


@router.get("/test_connection")
async def test_connection():
    return await films_service.test_connection()


@router.get("/films/{id}")
async def get_film(id: str):
    return await films_service.get_film(id)
