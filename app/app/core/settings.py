from pydantic import BaseSettings


class APISettings(BaseSettings):
    title: str = "Cashback"
    description: str = "Cashback api for test propouse"
    version: str = "1.0.0"
    api_version_str = "/api/v1"

    class Config:
        env_file = ".env"


class ServerSettings(BaseSettings):
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = True

    class Config:
        env_file = ".env"


class MongoDBSettings(BaseSettings):
    username: str = "admin"
    password: str = "admin"
    database: str = "cashback"
    url: str = "localhost"

    class Config:
        env_file = ".env"
