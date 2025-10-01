from datetime import datetime
import json
import requests

from struc.responseStruc import ResponseStruc
from utils.Token import getToken


GET_URL = "https://playground.api.lazycat.cloud/cms/review?page=0&size=100&sort=-updatedAt&keyword="



def GetArticlePengdingData():
    """ 获取代审核文章数据 """
    token = getToken()

    HEADERS = {
        "Cookie": f"userToken={token}"
    }
    TODAY = datetime.now().date()
    
    reponse = requests.get(GET_URL, headers=HEADERS)
    result = ResponseStruc()


    if (reponse.status_code == 200):
        reponse_json = reponse.json()
        reponse_json_items = reponse_json['items']
        res = set()
        if (len(reponse_json_items) > 0):
            for item in reponse_json_items:
                title = item["title"]
                nickName = item["user"]["nickname"]
                updatedAt = item["updatedAt"]
                
                if updatedAt == None or updatedAt == "":
                    continue
                updated_time = updatedAt.split("T")[0]
               
                # 跳过今天提交的
                if updated_time == TODAY:
                    continue

                res.add(json.dumps({
                    "title": title,
                    "nickname": nickName
                }))
        result.code = 200
        result.data = [json.loads(s) for s in res]
    elif (reponse.status_code == 401):
        result.code = 401
    else:
        result.code = 500
    return result


GetArticlePengdingData()

