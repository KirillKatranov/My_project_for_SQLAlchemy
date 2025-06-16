import datetime
from enum import Enum
from typing import Annotated
from sqlalchemy import  String, func, text
from database import Base, str_500
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class ContentSource(Enum):
    vk = "vk"
    tg = "tg"
    yt = "yt"
    site = "site"

class ContentOrm(Base):
    __tablename__ = "content"
    id: Mapped[intpk] = mapped_column(primary_key=True)
    link: Mapped[str_500] = mapped_column(String(500))
    source: Mapped[ContentSource]
    topic: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[created_at]