from beanie import Document


class Token(Document):
    token_type: str
    access_token: str
    refresh_token: str

    class Collection:
        name = "token"

    class Config:
        schema_extra = {
            "example": {
                "acess_token": "access_token",
                "refresh_token": "refresh_token",
            }
        }


class UserAuth(Document):
    email: str | None = None
    password: str | None = None

    class Collection:
        name = "user_auth"

    class Config:
        schema_extra = {
            "example": {
                "email": "admin",
                "password": "teste"
            }
        }


class UserOut(Document):
    id: str | None = None
    email: str | None = None

    class Collection:
        name = "user_out"

    class Config:
        schema_extra = {
            "example": {
                "id": "123456789",
                "email": "teste@teste.com.br"
            }
        }
