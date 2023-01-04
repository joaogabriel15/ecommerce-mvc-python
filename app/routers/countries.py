from fastapi import APIRouter, Request
from controllers.country_controller import CountryController
from models.database import session_async

from pydantic import BaseModel

router = APIRouter()


@router.get("/countries/", tags=['countries'])
async def list_countries():
    async with session_async() as session:
        db = CountryController(session)

        return await db.get_countries()


@router.post("/countries/create", tags=['countries'])
async def create_country(request: Request):

    return await request.json()
