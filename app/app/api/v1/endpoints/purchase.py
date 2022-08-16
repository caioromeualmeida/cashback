import httpx
from fastapi import APIRouter, Body, HTTPException
from fastapi_pagination import Page, paginate

from app.crud.purchase import Purchase
from app.crud.user import User
from app.service.purchase import add_purchase, list_purchase

router = APIRouter()


@router.post("/", response_model=Purchase)
async def new_purchase(purchase: Purchase = Body(...)):
    user_exists = await User.find_one(User.cpf == purchase.cpf)
    if not user_exists:
        raise HTTPException(
            status_code=409,
            detail="Cpf not found"
        )

    return await add_purchase(purchase)


@router.get("/cashback", description="Get accumulated cashback")
async def get_cashback(cpf: str):
    response = httpx.get(
        f'https://mdaqk8ek5j.execute-api.us-east-1.amazonaws.com/v1/cashback?cpf={cpf}')
    credit = response.json()['body']['credit']
    return {"cpf:": cpf, "cashback": credit}


@router.post("/{cpf}", response_model=Page[Purchase])
async def list(cpf: str):
    user_exists = await User.find_one(User.cpf == cpf)
    if not user_exists:
        raise HTTPException(
            status_code=409,
            detail="Cpf not found"
        )
    purchases = await list_purchase(cpf)
    return paginate(purchases)
