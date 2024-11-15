from pydantic import BaseModel


class Auth(BaseModel):
    email: str
    jwt: str
    uuid: str
