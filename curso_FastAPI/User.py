from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    password: str

    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "email": "test100@test.com",
                "password": "123456",

            }
        }




