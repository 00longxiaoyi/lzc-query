from typing import Any
from pydantic import BaseModel

class ResponseStruc(BaseModel):
    code: int = 500
    error: str | None = None
    data: Any | None = None
