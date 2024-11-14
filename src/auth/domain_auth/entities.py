from pydantic import BaseModel


class UserCommon(BaseModel):
    user_id: str
    username: str
    first_name: str
    phone: str
    address: str
    email: str


class User(UserCommon):
    password: str


class Auth(BaseModel):
    email: str
    jwt: str
    uuid: str
