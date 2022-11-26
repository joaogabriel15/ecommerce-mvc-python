from sqlalchemy.future import select
from sqlalchemy.orm import  Session
from models.User import User

class UserController():
    def __init__(self, db_session=Session):
        self.db_session = db_session
    

    async def get_users(self, User=User):
        # Buscas todos os usuarios do banco de dados
        stmt = select(User)
        response = await self.db_session.execute(stmt)  
        
        return response.all()

    def get_user():
        # Busca um usuario especifico
        pass
    
    def post_user():
        # Adiciona um usuario
        pass
    
    def del_user():
        # Deleta um usuario
        pass

    def put_user():
        # Altera um usuario
        pass