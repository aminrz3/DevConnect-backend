from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENV: str = "dev"
    DEBUG: bool = True
    DATABASE_URL: str
    REDIS_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
