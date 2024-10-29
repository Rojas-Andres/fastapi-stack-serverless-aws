from datetime import datetime
from typing import Any, Dict, Optional

from pydantic import BaseModel


class Log(BaseModel):
    api: str
    timestamp: str
    status_code: int
    response_body: str
    request_body: Optional[Dict[str, Any]] = None
    params: Optional[Dict[str, Any]] = None
    url: str
