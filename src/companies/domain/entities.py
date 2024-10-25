from pydantic import BaseModel
from typing import Optional


class Company(BaseModel):
    company_id: str
    name: str
    address: Optional[str]
