from typing import Optional

from pydantic_settings import BaseSettings


class SettingsPostgres(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_USER: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    class Config:
        case_sensitive = False
        env_file = ".env"


settings = SettingsPostgres()
