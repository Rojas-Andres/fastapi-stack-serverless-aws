from pydantic import BaseModel


class User(BaseModel):
    user_id: str
    username: str
    password: str
    first_name: str
    phone: str
    address: str
