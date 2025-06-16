import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine, text
from config import settings


sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool=5
)

session_factory = sessionmaker(sync_engine)

# with sync_engine.connect() as conn:
#     stmt = "CREATE TABLE news (news_id INT, link VARCHAR(100), source VARCHAR(100))"
#     conn.execute(text(stmt))
#     conn.commit()

str_500 = Annotated[str, 500]
class Base(DeclarativeBase):
    type_annotaded_map ={
        str_500: String(500)
    }
