from struc.articleData import get_article_data
from struc.moneyDataFunc import get_money_list_data
from struc.responseStruc import ResponseStruc
from struc.softDataFunc import get_sortware_data
from utils.FormatText import FormatTextOfUnionType
from utils.inspectionGetSoftAndArticleData import InspectDataExists


async def GetSummaryData(curTime:str, tomorrow: str):
    """
    获取文稿和应用汇总的文本数据
    Returns:
       result ResponseStruc 
    """
    result = ResponseStruc(
        code=200
    )

    monenydata = await get_money_list_data()

    if len(monenydata) == 0:
        result.code = 500
        result.error = "金额类别为0,请先设置金额列表"
        return result

    try:
        await InspectDataExists(curTime, tomorrow)
        articleData = await get_article_data()
        softData = await get_sortware_data()

        data = await FormatTextOfUnionType(softData, articleData)
        result.data = data
    except Exception as e:
        result.code = 500
        result.error = str(e)
    return result
