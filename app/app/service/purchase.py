

from datetime import date, datetime

from app.crud.purchase import Purchase


async def get_month_cashback(cpf):
    dt_ini = datetime(day=1, month=date.today().month, year=date.today().year)
    dt_fin = datetime(day=date.today().day, month=date.today(
    ).month, year=date.today().year, hour=23, minute=59, second=59)

    return await Purchase.find({
        "cpf": cpf,
        "date": {'$lte': dt_fin, '$gte': dt_ini}
    }).sum(Purchase.value)


async def add_purchase(new_purchase: Purchase):
    if new_purchase.cpf == "15350946056":
        new_purchase.status = "Aprovado"

    cashback = await get_month_cashback(new_purchase.cpf)
    if cashback:
        if new_purchase.value <= 1000:
            new_purchase.cashback = (new_purchase.value/cashback * 0.10)*100
        elif new_purchase.value <= 1500:
            new_purchase.cashback = (new_purchase.value/cashback * 0.15)*100
        else:
            new_purchase.cashback = (new_purchase.value/cashback * 0.20)*100

    return await new_purchase.create()


async def list_purchase(cpf: str):
    return await Purchase.find(Purchase.cpf == cpf).to_list()
