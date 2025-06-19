
import time
from database import sync_engine, Base, session_factory
from models import ContentOrm, PlatformContentSource, SourceORM



def create_tables():
    sync_engine.echo = True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True

def insert_data():
    with session_factory() as session:
        news_buttefly = ContentOrm(
            topic="Экосистемы c обилием бабочек лучше адаптировались к внезапным засухам",
            link="https://nplus1.ru/news/2025/06/11/flash-froughts",
            platform_source_enum=PlatformContentSource.vk
            )
        session.add(news_buttefly)
        session.commit()

def insert_data_source(source: str):
    with session_factory() as session:
        source = SourceORM(source_link=source[0])
        session.add(source)
        session.commit()


def insert_data_vk(filtered_content: dict):
    with session_factory() as session:
        content = ContentOrm(**filtered_content)
        session.add(content)
        #session.refresh()
        session.commit()

def update_data_vk():
    content_id = 1
    with session_factory() as session:
        content = session.get(ContentOrm, content_id)
        time.sleep(25)
        session.refresh(content)
        content.topic = "Какой то заголовок"
        session.commit()