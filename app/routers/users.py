from fastapi import APIRouter
from controllers.user_controller import UserController
from models.database import session_async

router = APIRouter()


@router.get("/users/", tags=["users"])
async def list_all_users():
    async with session_async() as session:
        db = UserController(session)
        return await db.get_users()


@router.get("/users/{id}")
async def get_user(id):
    async with session_async() as session:
        db = UserController(session)
        return await db.get_user(id)
