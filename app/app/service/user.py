

from app.core.utils import encript_password
from app.crud.user import User


async def get_user(username: str):
    return await User.find_one(User.email == username)


async def add_user(new_user: User):
    new_user.password = await encript_password(new_user.password)
    return await new_user.create()
