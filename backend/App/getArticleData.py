from typing import List
import requests

from struc.articleData import set_article_data
from struc.responseStruc import ResponseStruc
from struc.software import ArticleDataStruc
from utils.FormatText import FormatTextOfSingleType
from utils.Token import getToken

async def GetArticleData(startDay, endDay):
    """ 获取已审核的文章数据 """
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
        resList: List[ArticleDataStruc] = []

        if (items and len(items) > 0):
            for item in items:
                userId = item["user"]["id"] 
                title =   item["title"]
                nickname = item["user"]["nickname"]

                resList.append(ArticleDataStruc(
                    id=f"article_{len(resList)+1}",
                    user_id=userId,
                    nick_name=nickname,
                    name=title
                ))

        data = await FormatTextOfSingleType(resList)
        #await saveArticleData(resList)
        await set_article_data(resList)

        result.code = 200
        result.data = data
    elif (response.status_code == 401):
        result.code = 401
        result.error = "登录状态已失效"
    else:
        result.code = 500
    return result
