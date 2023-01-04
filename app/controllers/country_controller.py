from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.Country import Country


class CountryController():
    def __init__(self, db_session=Session):
        self.db_session = db_session

    async def get_countries(self):
        stmt = select(Country)
        response = await self.db_session.execute(stmt)

        return response.all()

    async def post_country(self, country=Country):
        self.db_session.add(country)
        response = self.db_session.commit()

        return response
