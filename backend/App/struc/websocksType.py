
from dataclasses import dataclass
from typing import Literal


@dataclass
class WsSendJsonInfo:
    type: Literal["error", "success", "warning"]
    data: str
