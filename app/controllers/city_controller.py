from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.City import City


class CityController():
    def __init__(self, db_session=Session):
        self.db_session = db_session

    async def get_cities(self):
        stmt = select(City)
        response = await self.db_session.execute(stmt)

        return response.all()
