from datetime import datetime

from beanie import Document
from bson.objectid import ObjectId


class Purchase(Document):
    value: float = 0.0
    date: datetime
    cpf: str | None = None
    status: str = "Em validação"
    cashback: float = 0.0
    
    class Collection:
        name = "purchase"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "value": 100.00,
                "date": datetime.now(),
                "cpf": "40630556806",
                "status": "Em Validação"
            }
        }
