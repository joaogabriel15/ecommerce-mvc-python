from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.State import State
from pydantic import BaseModel


class StateBody(BaseModel):
    id: int
    countryId: int
    description: str
    intials: str | None = None


class StateController():
    def __init__(self, db_session=Session):
        self.db_session = db_session

    async def get_states(self):
        stmt = select(State)
        response = await self.db_session.execute(stmt)

        return response.all()

    async def post_state(self, state: StateBody):

        response = await self.db_session.execute(state)

        return response.all()
