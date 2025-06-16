from database import sync_engine, Base, session_factory
from models import ContentOrm, ContentSource

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
            source=ContentSource.site
            )
        session.add(news_buttefly)
        session.commit()
