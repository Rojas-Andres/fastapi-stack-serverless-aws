from typing import Optional

from pydantic import BaseModel


class CompanyCreate(BaseModel):
    name: str
    address: Optional[str] = None
