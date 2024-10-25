from pydantic import BaseModel
from typing import Optional


class CompanyCreate(BaseModel):
    name: str
    address: Optional[str] = None
