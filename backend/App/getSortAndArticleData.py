from typing import List

from struc.articleData import get_article_data
from struc.moneyDataFunc import get_money_list_data
from struc.responseStruc import ResponseStruc
from struc.softDataFunc import get_sortware_data
from struc.software import CompletedDataStruc
from utils.inspectionGetSoftAndArticleData import InspectDataExists

async def GetSortAndArticleData(curTime: str, tomorrow: str) -> ResponseStruc:
    """
    Args: curTime str: 当前时间 
        tomorrow str: 下一天的时间
        时间格式: xxxx-xx-xx
    Returns:
        return ResponseStruc: 
            合并之后的应用和文章数据
    """
    result = ResponseStruc(
        code=200
    )
    try:
       await InspectDataExists(curTime, tomorrow) 
    except Exception as e:
        result.code = 500
        result.error = str(e)
    # 获取数据
    resultData = await mergeData()
    result.data = resultData
    return result

async def mergeData() -> List[CompletedDataStruc]:
    softwareData = await get_sortware_data()
    articleData = await get_article_data()
    moneyData = await get_money_list_data()

    moneyDataJson = {item.id: item for item in moneyData} 

    resultList: List[CompletedDataStruc] = []
    for i in softwareData:
        resultList.append(CompletedDataStruc(
            id=i.id,
            user_id=i.user_id,
            name=i.name,
            nick_name=i.nick_name,
            type="soft",
            money=(m.money if (m := moneyDataJson.get(i.id)) else 100)
        ))

    for i in articleData:
        resultList.append(CompletedDataStruc(
            id=i.id,
            user_id=i.user_id,
            name=i.name,
            nick_name=i.nick_name,
            type="aritlce",
            money=(m.money if (m := moneyDataJson.get(i.id)) else 50)
        ))

    return resultList
