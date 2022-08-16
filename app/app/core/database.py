from tokenize import Token

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core import mongodb_settings
from app.crud.auth import Token, UserAuth
from app.crud.purchase import Purchase
from app.crud.user import User

mongodb_settings.username = "admin"
MONGODB_URL = f"mongodb://{mongodb_settings.username}:{mongodb_settings.password}@{mongodb_settings.url}/{mongodb_settings.database}?retryWrites=true&w=majority"

client = None


async def create_client():
    client = AsyncIOMotorClient(MONGODB_URL)
    await init_beanie(database=client.get_default_database(), document_models=[User, UserAuth, Token, Purchase])


async def free_client():
    client.close()
