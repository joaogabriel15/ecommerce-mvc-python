from fastapi import APIRouter
from controllers.states_controller import StateController
from models.database import session_async

router = APIRouter()


@router.get("/states/", tags=["states"])
async def list_states():
    async with session_async() as session:
        db = StateController(session)
        return await db.get_states()


@router.post("/states/create", tags=["states"])
async def create_state():
    async with session_async as session:
        db = StateController(session)
