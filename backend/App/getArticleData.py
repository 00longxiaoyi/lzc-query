


import requests

from struc.responseStruc import ResponseStruc
from utils.FormatText import FormatText
from utils.Token import getToken




def GetArticleData(startDay, endDay):

    token = getToken()
    HEADERS = {
        "Cookie": f"userToken={token}"
    }

    GET_URL = f"https://playground.api.lazycat.cloud/cms/guideline?page=0&size=100&sort=-id&keyword=&published=true&reviewedAt_start={startDay} 00:00:00&reviewedAt_end={endDay} 00:00:00" 
    response = requests.get(GET_URL, headers=HEADERS)
    result = ResponseStruc()
    if (response.status_code == 200):
        
        response_json = response.json()
        items = response_json["items"]
        res = {}
        if (items and len(items) > 0):
            for item in items:
                userId = item["user"]["id"] 
                title =   item["title"]
            
                if (userId in res.keys()):
                    res[userId].append([title])
                else:
                    res[userId] = [[title]]
            
        data = FormatText("article.txt", startDay, res, "article")
        result.code = 200
        result.data = data
    elif (response.status_code == 401):
        result.code = 401
    else:
        result.code = 500
    return result
