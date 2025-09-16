from datetime import datetime
import json
import requests

from struc.responseStruc import ResponseStruc
from utils.Token import getToken

def GetSoftwarePendingData():
    token = getToken()  
    COOKIE=f"userToken={token}"
    PARAMS = {
        "sort": "-id",
        "page": 0,
        "size": 100,
        "filters": '["status","=","0"]'
    }
    URL=f"https://appstore.api.lazycat.cloud/api/v3/admin/review/app/list?sort={PARAMS['sort']}&page={PARAMS['page']}&size={PARAMS['size']}&filters={PARAMS['filters']}"
    HEADERS={
        "Cookie": COOKIE,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0",
    }
    
    CUR_TIME = datetime.now().strftime("%Y-%m-%d")
    
    response = requests.get(URL, headers=HEADERS)
    print(response.status_code)
    result = ResponseStruc()
    if (response.status_code == 200):
        response_json = response.json()
        if "items" in dict(response_json).keys():
            res = set()
            for item in response_json["items"]:
                updated_at = item["updated_at"]
                
                if updated_at == None or updated_at == "":
                    continue
                updated_time = updated_at.split("T")[0]
               
                # 跳过今天提交的
                if updated_time == CUR_TIME:
                    continue
    
                resource = None
                name = ""
                nickname = ""
                
                if item['resource'] is None:
                    resource = item['app']['resource']
                else:
                    resource = item['resource']
                
                name = resource['info_data'].get('zh', {}).get('name') or resource['info_data'].get('en', {}).get('name')
                nickname = item['create_user']['nickname']
                
                res.add(json.dumps({
                    "title": name,
                    "nickname": nickname
                }))
            result.code = 200
            result.data = [json.loads(s) for s in res]
            return result
    elif (response.status_code == 401):
        result.code = 401
        return result
    else:
        return result
