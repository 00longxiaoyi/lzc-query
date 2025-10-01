""" 获取已审核应用数据 """
from typing import List
import requests
from struc.responseStruc import ResponseStruc
from struc.software import TempPicInfoStruc
from utils.FormatText import FormatText
from utils.Token import getToken 

from utils.data import set_pic_data 


APP_URL = "https://appstore.api.lazycat.cloud/api/v3/admin/app/list"

DEVUSER_URL = "https://appstore.api.lazycat.cloud/api/v3/admin/developer?sort=-id&page=0&size=20&user_id="

async def GetContent(start_time: str, end_time: str):
    """ 获取已审核的应用数据 """
    token = getToken()
    HEADERS = {
        "Cookie": f"userToken={token}"
    }
 
    START_TIME = f"{start_time} 00:00:00"
    END_TIME = f"{end_time} 00:00:00"

    QUERY_CONTENT = {
        "sort": "-id",
        "page": 0,
        "size": 100,
        "seek": "",
        "filter": '["status","=","1"]',
        "version_updated_at_start": START_TIME,
        "version_updated_at_end": END_TIME
    }

    reuslt = {}
    pics: List[TempPicInfoStruc] = []
    reponse = ResponseStruc()
    res = requests.get(APP_URL, headers=HEADERS, params=QUERY_CONTENT)
    print(res.url)
    if (res.status_code == 200):
        res_list = res.json()['items']
        # create_user -> id
        # info_data -> zh -> name
        # info_data -> zh -> screenshot_pc_paths[0]
        for item in res_list:
            user_id = item["create_user"]["id"]
            # 简介
            brief = ""
            software_name = ""
            pic: TempPicInfoStruc = TempPicInfoStruc() 

            # 详细信息
            soft_info = {}

            if ("zh" in item['resource']["info_data"].keys()):
                soft_info = item['resource']["info_data"]["zh"]
            else:
                soft_info = item['resource']["info_data"]["en"]

            if len(soft_info.keys()) > 0:
                software_name = soft_info['name']
                if (soft_info['screenshot_pc_paths'] and len(soft_info['screenshot_pc_paths']) > 0):
                    pic.url = soft_info['screenshot_pc_paths'][0]
                    pic.name = software_name
                brief = soft_info['brief']

            if (user_id in reuslt.keys()):
                reuslt[user_id].append([software_name, brief])
            else:
                reuslt[user_id] = [[software_name, brief, len(pics) + 1]]
            if (pic.name and pic.url):
                pics.append(pic)
        data = FormatText("software.txt", start_time, reuslt, "software")
        # 保存临时图片数据 
        await set_pic_data(pics)
        #SaveFormatTempPicsInfo(pics)

        reponse.code = 200
        reponse.data = data
        print(reponse)
        return reponse
    else:
        print(f"数据获取失败")
