from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = ""

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(bind=engine, class_= AsyncSession)

async def get_db():
    async with async_session as session:
        yield session

Base = declarative_base()