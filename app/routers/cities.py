from fastapi import APIRouter
from controllers.city_controller import CityController
from models.database import session_async

router = APIRouter()


@router.get("/cities/", tags=['cities'])
async def list_all_cities():
    async with session_async() as session:
        db = CityController(session)
        return await db.get_cities()
