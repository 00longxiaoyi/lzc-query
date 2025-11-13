import asyncio
from typing import Any, List

from error.errorType import IDNotFoundError
from struc.dataLoadStatus import Change_software_and_article_data_status
from struc.software import ArticleDataStruc


article_data:List[ArticleDataStruc] = []
article_data_lock = asyncio.Lock()

async def set_article_data(data: List[ArticleDataStruc]):
    """ 设置文章数据 """
    global article_data 
    async with article_data_lock:
        article_data = data
        # 去同步状态
        await Change_software_and_article_data_status(2)

async def change_article_data_of_key(id:str, key: str, value: Any):
    """ 设置文章数据 """
    global article_data
    isExists = False
    async with article_data_lock:
        for i in article_data:
            if (i.id == id):
                setattr(i, key, value)
                isExists = True
                break
        if not isExists:
            raise IDNotFoundError(f"id 不存在 {id}")

async def get_article_data() -> List[ArticleDataStruc]:
    """ 获取文章数据 """
    async with article_data_lock:
        return article_data
