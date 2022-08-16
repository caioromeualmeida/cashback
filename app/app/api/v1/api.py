from fastapi import APIRouter, Depends

from app.api.v1.endpoints import auth, purchase, user
from app.service.auth import get_current_user

api_router = APIRouter()
api_router.include_router(auth.router, tags=["auth"], prefix="/auth")
api_router.include_router(user.router, tags=[
                          "user"], prefix="/user", dependencies=[Depends(get_current_user)])
api_router.include_router(purchase.router, tags=[
                          "purchase"], prefix="/purchase", dependencies=[Depends(get_current_user)])
