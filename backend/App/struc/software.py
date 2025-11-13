
from pydantic.dataclasses import dataclass
from typing import Literal,  Union


@dataclass
class TempPicInfoStruc():
    name: str = ""
    url: str = ""

@dataclass
class MoenyDataStruc():
    id: str
    money: int

@dataclass
class CompletedDataStruc():
    id: str
    user_id: Union[int, str]
    name: str
    nick_name: str
    type: Literal["soft", "aritlce"]
    money: int

@dataclass
class SoftwareDataStruc():
    id: str
    user_id: Union[int, str]
    nick_name: str
    brief: str
    name: str

@dataclass
class ArticleDataStruc():
    id: str
    user_id: Union[int, str] 
    nick_name: str
    name: str
