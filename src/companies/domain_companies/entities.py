from typing import Optional

from pydantic import BaseModel


class Company(BaseModel):
    company_id: str
    name: str
    address: Optional[str]
