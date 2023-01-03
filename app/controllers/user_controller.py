from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models.User import User


class UserController():
    def __init__(self, db_session=Session):
        self.db_session = db_session

    async def get_users(self):
        # Buscas todos os usuarios do banco de dados
        stmt = select(User)
        response = await self.db_session.execute(stmt)

        return response.all()

    async def get_user(self, id):
        # Busca um usuario especifico
        stmt = select(User).where(User.id.cast == id)
        response = await self.db_session.execute(stmt)

        return response.all()

    def post_user(self):
        # Adiciona um usuario
        pass

    def del_user(self):
        # Deleta um usuario
        pass

    def put_user(self):
        # Altera um usuario
        pass
