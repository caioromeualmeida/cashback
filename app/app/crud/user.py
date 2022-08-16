from beanie import Document


class User(Document):
    email: str | None = None
    cpf: str | None = None
    name: str | None = None
    password: str

    class Collection:
        name = "user"

    class Config:
        schema_extra = {
            "example": {
                "email": "teste@teste.com",
                "cpf": "40630556993",
                "name": "caio romeu",
                "password": "teste"
            }
        }
