import asyncio
from typing import Any, List

from error.errorType import IDNotFoundError
from struc.dataLoadStatus import Change_software_and_article_data_status
from struc.software import SoftwareDataStruc


software_data:List[SoftwareDataStruc] = []
software_data_lock = asyncio.Lock()

async def set_software_data(data: List[SoftwareDataStruc]):
    """ 设置应用数据 """
    global software_data
    async with software_data_lock:
        software_data = data
        # 同步状态
        await Change_software_and_article_data_status(1)

async def change_software_data_of_key(id: str, key: str, value: Any):
    """ 修改数据 """
    global software_data
    isExists = False
    async with software_data_lock:
        for i in software_data:
            if (i.id == id):
                setattr(i, key, value)
                isExists = True
                break
        if not isExists:
            raise IDNotFoundError(f"ID 不存在 {id}")

async def get_sortware_data() -> List[SoftwareDataStruc]:
    """ 获取应用数据 """
    async with software_data_lock:
        return software_data



