# 文本写入
from datetime import datetime
import json
from typing import Any, Dict, List, Union

from error.errorType import IDNotFoundError
from struc.moneyDataFunc import get_money_list_data
from struc.software import ArticleDataStruc, SoftwareDataStruc, TempPicInfoStruc
from utils.getUserInfo import GetDevUserInfo

async def FormatTextOfSingleType(data: Union[List[SoftwareDataStruc], List[ArticleDataStruc]]):
    # 格式化
    jsonData = await MergeData(data)
    return getResultText(jsonData)

async def FormatTextOfUnionType(softdata: List[SoftwareDataStruc], articleData: List[ArticleDataStruc]) -> str:
    softDataJson = await MergeData(softdata, True)
    articleDataJson = await MergeData(articleData, True)
    jsonData = MergeJsonData(softDataJson, articleDataJson)
    return getResultText(jsonData, True)

def getResultText(jsonData: Dict[str, List[Any]], isMoney=False) -> str:
    if isMoney:
        date_str = datetime.now().strftime("%Y年%-m月%-d日")
        result = f"""
--- {date_str} ---
今日移植应用及攻略总价值: xxx元
平均移植应用数量：x个
总应用数量：x个
更新应用个数：x个
应用涉及用户：x位



"""
    else:
        result = ""

    for key, items in jsonData.items():
        userInfo = GetDevUserInfo(str(key))
        if isMoney:
            sumMoney = sum(item.get('money', 0) for item in items) 
            result += f"@{userInfo} -{sumMoney}元\n"
        else:
            result += f"@{userInfo}\n"

        for item in items:
            result += f"- {item['name']}: {item['brief']}{' -' + str(item['money']) + '元' if isMoney else ''}\n"
        result += "\n"
    return result

def MergeJsonData(jsonData1: Dict[str, List[Any]], jsonData2: Dict[str, List[Any]]) -> Dict[str, List[Any]]:
    """合并两个dict数据
    Args:
        jsonData1
        jsonData2
    Returns:
        Dict: 新的dict数据
    """
    result = {}
    for k in set(jsonData1) | set(jsonData2):
        result[k] = jsonData1.get(k, []) + jsonData2.get(k, [])
    return result

async def MergeData(data: Union[
              List[SoftwareDataStruc], 
              List[ArticleDataStruc]], isMoney=False) -> Dict[str, List[Any]]:
    """ 合并数据
        data: Union[List[SoftwareDataStruc], List[ArticleDataStruc]: 数据
    Returns:
        dict: 返回的数据 
    """
    result = {}
    moneyDataJson = {}
    # 获取money的数据
    if isMoney:
        try:
            moneyData = await get_money_list_data()
            for money in moneyData:
                moneyDataJson[money.id] = money.money
        except Exception:
            raise
    try:
        for i in data:
            if i.user_id not in result.keys():
                result[i.user_id] = [getResultContent(i, isMoney, moneyDataJson)]
            else:
                result[i.user_id].append(getResultContent(i, isMoney, moneyDataJson))
    except Exception:
        raise

    return result


def getResultContent(data: Union[SoftwareDataStruc, ArticleDataStruc], isMoney=False, moneyData=dict()):
    if isinstance(data, SoftwareDataStruc):
        return softwareResult(data, isMoney, moneyData)
    if isinstance(data, ArticleDataStruc):
        return articleResult(data, isMoney, moneyData)

def softwareResult(data: SoftwareDataStruc,isMoney:bool,moneyData=dict()) -> dict:
    """ 获取应用结构
    Args:
       data SoftwareDataStruc: 应用数据
       isMoney boolean: 是否需要包含金额
       moneyData: 金额数据
    Returns:
       dict(): 结果 
    """
    result = {"name": data.name, "brief": data.brief}
    if isMoney:
        try:
            result["money"] = moneyData.get(data.id)
        except Exception:
            raise IDNotFoundError(f"获取金额数据时ID为空")

    return result

def articleResult(data: ArticleDataStruc, isMoney=False, moneyData=dict()) -> dict:
    """ 获取攻略结构
    Args:
       data ArticleDataStruc: 攻略数据
       isMoney boolean: 是否需要包含金额
       moneyData: 金额数据
    Returns:
       dict(): 结果 
    """
    result = {"name": "玩机攻略", "brief": data.name}
    if isMoney:
        try:
            result["money"] = moneyData.get(data.id)
        except Exception:
            raise IDNotFoundError(f"获取金额数据时ID为空")

    return result


def SaveFormatTempPicsInfo(info: List[TempPicInfoStruc]):
    """ 保存临时数据 """
    if (info == "" or info == None): return
    try:
        with open("./files/tempPicsInfo.json", "w", encoding="utf-8") as f:
            json.dump(info, f,default=lambda o: o.__dict__, ensure_ascii=False, indent=4)
    except Exception as e:
        raise e

def LoadingFormantTempPicsInfo() -> List[TempPicInfoStruc]:
    """ 读取临时数据 """
    try:
        with open("./files/tempPicsInfo.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return [TempPicInfoStruc(**item) for item in data]
    except Exception as e:
        raise e
