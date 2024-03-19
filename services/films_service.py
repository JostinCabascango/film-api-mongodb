from database import film_collection


async def get_film(id: str):
    pass


async def test_connection():
    document = await film_collection.find_one()
    return document
