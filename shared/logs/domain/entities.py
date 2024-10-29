from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime


class Log(BaseModel):
    api: str
    timestamp: str
    status_code: int
    response_body: str
    request_body: Optional[Dict[str, Any]] = None
    params: Optional[Dict[str, Any]] = None
    url: str
