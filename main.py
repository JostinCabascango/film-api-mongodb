from fastapi import FastAPI
from routers import films

# Create an instance of the FastAPI class.
app = FastAPI(
    title="Film API",
    description=(
        "This is a simple API that allows you to manage films. "
        "You can perform CRUD operations on films and also filter, sort and limit the films. "
        "The API uses MongoDB as its database."
    ), version="1.0.0",
)
# Include the films router.
app.include_router(
    films.router,
    prefix="/api",
    tags=["films"],
    responses={404: {"description": "Not found"}},
)
