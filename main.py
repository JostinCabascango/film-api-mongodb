from fastapi import FastAPI

from routers import films

app = FastAPI()

app.include_router(films.router)
