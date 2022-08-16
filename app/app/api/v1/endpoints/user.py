from fastapi import APIRouter, Body, HTTPException

from app.crud.user import User
from app.service.user import add_user

router = APIRouter()


@router.post("/", response_model=User)
async def new_user(user: User = Body(...)):
    user_exists = await User.find_one(User.email == user.email)
    if user_exists:
        raise HTTPException(
            status_code=409,
            detail="User supplied already exists"
        )

    return await add_user(user)
