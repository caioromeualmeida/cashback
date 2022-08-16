

from datetime import datetime

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt

from app.core.utils import (ALGORITHM, JWT_SECRET_KEY, encript_password,
                            oauth2_scheme, verify_password)
from app.crud.auth import UserAuth
from app.crud.user import User


async def get_user_auth(username: str):
    return await UserAuth.find_one(UserAuth.email == username)


async def add_user_auth(new_user: UserAuth):
    new_user.password = await encript_password(new_user.password)
    return await new_user.create()


async def authenticate(username: str, password: str):
    user = await get_user_auth(username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        exp: str = payload.get("exp")
        if username is None:
            raise credentials_exception

        if datetime.fromtimestamp(exp) < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except JWTError:
        raise credentials_exception
    user = await get_user_auth(username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user
