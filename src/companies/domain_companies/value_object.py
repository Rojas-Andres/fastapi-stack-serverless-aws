from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str
