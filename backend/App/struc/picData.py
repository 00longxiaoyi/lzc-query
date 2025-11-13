import asyncio
from typing import List
from struc.software import MoenyDataStruc, TempPicInfoStruc

data_tmp_pics:List[TempPicInfoStruc] = []
data_lock = asyncio.Lock()

moeny_data: List[MoenyDataStruc] = []
moeny_data_lock = asyncio.Lock()

async def set_pic_data(pics: List[TempPicInfoStruc]):
    global data_tmp_pics
    async with data_lock:
        data_tmp_pics = pics

async def get_pic_data() -> List[TempPicInfoStruc]:
    async with data_lock:
        return data_tmp_pics


