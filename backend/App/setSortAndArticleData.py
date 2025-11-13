from typing import List

from struc.moneyDataFunc import get_money_list_data, set_money_list_data
from struc.responseStruc import ResponseStruc
from struc.software import CompletedDataStruc, MoenyDataStruc

async def SetMoneyData(data: List[CompletedDataStruc]) -> ResponseStruc:
    """
    设置应用、文章的数据
    Args:
        data List[CompletedDataStruc]: 汇总数据
    Returns:
        result ResponseStruc: 设置的结果 
    """
    result = ResponseStruc(
        code=200
    )

    moneyData = await get_money_list_data()
    moneyDataJson = {m.id: m for m in moneyData}
    try:
        for i in data:
            m = moneyDataJson.get(i.id)
            if m:
                m.money = i.money or 0
            else:
                # 第一次是注入
                moneyDataJson[i.id] = MoenyDataStruc(id=i.id, money=i.money)

        newMoenyData = [moneyDataJson[key] for key in moneyDataJson.keys()]
        await set_money_list_data(newMoenyData)
    except Exception as e:
        result.code = 500
        result.error = "数据提交出错"

    return result 
