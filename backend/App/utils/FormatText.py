# 文本写入
import json
import os
from typing import List
from struc.software import TempPicInfoStruc
from utils.getUserInfo import GetDevUserInfo

FILE_DIR = "./files/pics/"

def FormatText(fileName: str, dirname:str, content: dict, type: str):
    # 格式化
    result = ""
    for key in content.keys():
         # 同步用户名称和群号
        userInfo = GetDevUserInfo(str(key))
        result += f"@{userInfo}\n"
        for item in content[key]:
            if (type == "software"):
                result += f" - {item[1]} ({item[0]}) \n"
            if (type == "article"):
                result += f" - 玩机攻略：{item[0]} \n "

        result += "\n"
    if not (os.path.exists(f"{FILE_DIR}{dirname}")):
        os.makedirs(f"{FILE_DIR}{dirname}")
    with open(f"{FILE_DIR}{dirname}/{fileName}", 'w', encoding="utf-8") as f:
        f.write(result)
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
