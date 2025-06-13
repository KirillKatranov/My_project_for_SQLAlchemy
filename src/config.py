from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings): #Автоматически подгружает переменные окружения или переменные из .env 
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property #Если вызвать например Settings().DATABASE_URL_asyncpg, то вызовется этот метод
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    model_config = SettingsConfigDict(env_file=".env") # .env должен лежать в корне проекта и подгружать значения именно из env
    #model_config = SettingsConfigDict() При такой конфигруации подключаемся из переменных окружения
settings = Settings()
