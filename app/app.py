from fastapi import FastAPI
import socket
from models import database
from models.database import engine, Base

from routers import users
from routers import states
from routers import countries

app = FastAPI(title="FastAPI Aplication Ecomerce")


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


app.include_router(users.router)
app.include_router(states.router)
app.include_router(countries.router)


@app.get("/")
async def read_root():
    return {"Name container is ruinning this": socket.gethostname()}
