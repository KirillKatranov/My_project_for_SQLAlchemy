import datetime
from enum import Enum
from typing import Annotated
from sqlalchemy import  ForeignKey, String, func, text
from database import Base, str_500
from sqlalchemy.orm import Mapped, mapped_column


intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]

class PlatformContentSource(Enum):
    vk = "vk"
    tg = "tg"
    yt = "yt"
    site = "site"

class ContentOrm(Base):
    """Готовый контент на отправку"""
    __tablename__ = "content"
    id: Mapped[intpk]
    link: Mapped[str_500]
    platform_source_enum: Mapped[PlatformContentSource]
    topic: Mapped[str] = mapped_column(String(500), nullable=True)
    created_at: Mapped[created_at]
    source: Mapped[int] = mapped_column(ForeignKey("source.source_link", ondelete="CASCADE"))

class SourceORM(Base):
    """Содержит выбранные пользователем источники(ссылки на них)"""
    __tablename__ = "source"
    #id: Mapped[intpk]
    source_link: Mapped[str_500] = mapped_column(primary_key=True)