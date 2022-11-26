import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from config import settings

SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True

)

    
session_async = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
