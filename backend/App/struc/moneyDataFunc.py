import asyncio
from typing import List
from error.errorType import IDNotFoundError
from struc.software import MoenyDataStruc


moneyListData: List[MoenyDataStruc] = []
moeny_list_data_lock = asyncio.Lock()

async def set_money_list_data(data: List[MoenyDataStruc]):
    """ 设置所有的金额列表
    Args:
       data List[MoenyDataStruc]: 金额列表 
    """
    global moneyListData
    async with moeny_list_data_lock:
        moneyListData = data


async def get_money_list_data() -> List[MoenyDataStruc]:
    """ 获取所有金额
    Returns:
       List[MoenyDataStruc]: 金额列表 
    """
    global moneyListData
    async with moeny_list_data_lock:
        return moneyListData

async def set_money_data_of_id(id: str, value: int):
    """ 设置单个金额
    Args:
       id str: id
       value int: 金额

    Error type: IDNotFoundError
    """ 
    global moneyListData
    isExists = False
    async with moeny_list_data_lock:
        for data in moneyListData:
            if data.id == id:
                data.money = value
                isExists = True
                break
        if not isExists:
            raise IDNotFoundError(f"ID 不存在 {id}") 

