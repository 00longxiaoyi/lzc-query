import asyncio
from typing import Literal


software_and_article_data_status = 0b00000000
software_and_article_data_status_lock = asyncio.Lock()

async def Get_sortware_and_article_data_status() -> int:
    """
    获取软件和文章数据是否已加载的状态码（位掩码）。
    Returns:
        int: 表示加载状态的位掩码（bitmask）。
             例如：
             - 0b00000001 (1): 软件数据已加载
             - 0b00000010 (2): 文章数据已加载
             - 0b00000011 (3): 软件和文章数据均已加载
    """
    async with software_and_article_data_status_lock:
        return software_and_article_data_status

async def Change_software_and_article_data_status(postion: Literal[1, 2]):
    """
    切换应用和文章目前是否下载过
    Args:
        postion Literal[1, 2]: 
            1 -> software get status
            2 -> article get status
    example:
        0b00000001: software status 1 表示应用的数据加载过
        0b00000011: article and software status 1 表示应用和文章的数据都加载过
    """
    global software_and_article_data_status 
    async with software_and_article_data_status_lock:
        # 将第N位改为1标记为已加载过
        # postion - 1 修正修改的位置
        software_and_article_data_status = software_and_article_data_status | ( 1 << postion - 1 )

