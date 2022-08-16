
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.core.utils import create_access_token, create_refresh_token
from app.crud.auth import Token, UserAuth
from app.service.auth import add_user_auth, authenticate, get_user_auth

router = APIRouter()


@router.post("/login", response_model=Token, response_description="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(
        form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {
        "token_type": "bearer",
        "access_token": create_access_token(data={"sub": user.email}),
        "refresh_token": create_refresh_token(data={"sub": user.email}),
    }


@router.post("/signup", response_model=UserAuth, response_description="Create new token")
async def create_user(data: UserAuth):
    user = await get_user_auth(data.email)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist",
            headers={"WWW-Authenticate": "Bearer"},
        )

    new_user = UserAuth()
    new_user.email = data.email
    new_user.password = data.password

    return await add_user_auth(new_user)
