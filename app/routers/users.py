from fastapi import APIRouter
from controllers.userController import UserController
from models.database import session_async

router = APIRouter()



@router.get("/users/", tags=["users"])
async def list_all_users():
    async with session_async() as session:
        response =   UserController(session)
        return await response.get_users()