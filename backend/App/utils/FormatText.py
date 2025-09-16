# 文本写入
import os
from utils.getUserInfo import GetDevUserInfo

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
    if not (os.path.exists(f"./pics/{dirname}")):
        os.makedirs(f"./pics/{dirname}")
    with open(f"./pics/{dirname}/{fileName}", 'w', encoding="utf-8") as f:
        f.write(result)
    return result
