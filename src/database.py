import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine, text
from config import settings


engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool=5
)

with engine.connect() as conn:
    stmt = "CREATE TABLE news (news_id INT, link VARCHAR(100), source VARCHAR(100))"
    conn.execute(text(stmt))
    conn.commit()
