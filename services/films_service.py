import pymongo
from bson import ObjectId
from fastapi import HTTPException

from database import create_mongo_connection

# Constants for the database name and collection name.
DATABASE_NAME = 'Films'
COLLECTION_NAME = 'Film'


def get_film_collection():
    """
    Establish a connection to the MongoDB instance and return the film collection.
    """
    try:
        client = create_mongo_connection()
        if client is None:
            raise HTTPException(status_code=500, detail="Failed to connect to MongoDB")
        database_name = DATABASE_NAME
        db = client[database_name]
        return db[COLLECTION_NAME]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def convert_id(film):
    """
    Convert the '_id' field from ObjectId to string and rename it to 'id'.
    """
    film['id'] = str(film['_id'])
    return film


async def get_all_films():
    """
     Retrieve all films from the database.
     """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    return [convert_id(film) for film in film_collection.find()]


async def get_film(id: str):
    """
     Retrieve a single film by its ID.
     """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    film = film_collection.find_one({"_id": ObjectId(id)})
    return convert_id(film) if film else None


async def create_film(film):
    """
       Add a new film to the database.
       """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    result = film_collection.insert_one(film.dict())
    return film if result.inserted_id else None


async def update_film(id, film):
    """
        Update a single film by its ID.
        """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    result = film_collection.update_one({"_id": ObjectId(id)}, {"$set": film.dict()})
    if result.modified_count > 0:
        updated_film = film_collection.find_one({"_id": ObjectId(id)})
        return convert_id(updated_film)
    return None


async def delete_film(id: str):
    """
       Remove a single film by its ID.
       """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    film = film_collection.find_one({"_id": ObjectId(id)})
    if film:
        film_collection.delete_one({"_id": ObjectId(id)})
        return convert_id(film)
    return None


async def get_films_by_genre(genre):
    """
       Retrieve films by genre.
       """
    film_collection = get_film_collection()
    if film_collection is None:
        return None
    return [convert_id(film) for film in film_collection.find({"genre": {"$regex": genre, "$options": "i"}})]


async def get_sorted_films(field: str, order: str):
    """
      Retrieve films sorted by a specific field and order.
    """
    if field not in ["title", "director", "year"]:
        raise HTTPException(status_code=400, detail="Invalid field parameter")
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter")
    sort_order = pymongo.ASCENDING if order == "asc" else pymongo.DESCENDING
    film_collection = get_film_collection()
    if film_collection is None:
        raise HTTPException(status_code=404, detail="No films found")
    return [convert_id(film) for film in film_collection.find().sort(field, sort_order)]


async def get_limited_films(limit: int):
    """
       Retrieve a limited number of films.

    """
    if limit < 1 or limit > 100:
        raise HTTPException(status_code=400, detail="Invalid limit parameter")
    film_collection = get_film_collection()
    if film_collection is None:
        raise HTTPException(status_code=404, detail="No films found")
    total_films = film_collection.count_documents({})
    return {"row_count": total_films, "data": [convert_id(film) for film in film_collection.find().limit(limit)]}
