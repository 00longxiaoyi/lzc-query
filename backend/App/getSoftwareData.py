import requests
import os
from struc.responseStruc import ResponseStruc
from utils.FormatText import FormatText
from utils.Token import getToken 


APP_URL = "https://appstore.api.lazycat.cloud/api/v3/admin/app/list"

DEVUSER_URL = "https://appstore.api.lazycat.cloud/api/v3/admin/developer?sort=-id&page=0&size=20&user_id="

def GetContent(start_time: str, end_time: str):
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
    pics = []
    reponse = ResponseStruc()
    res = requests.get(APP_URL, headers=HEADERS, params=QUERY_CONTENT)
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
            pic = ""

            # 详细信息
            soft_info = {}

            if ("zh" in item['resource']["info_data"].keys()):
                soft_info = item['resource']["info_data"]["zh"]
            else:
                soft_info = item['resource']["info_data"]["en"]

            if len(soft_info.keys()) > 0:
                software_name = soft_info['name']
                if (soft_info['screenshot_pc_paths'] and len(soft_info['screenshot_pc_paths']) > 0):
                    pic = soft_info['screenshot_pc_paths'][0]
                brief = soft_info['brief']

            if (user_id in reuslt.keys()):
                reuslt[user_id].append([software_name, brief])
            else:
                reuslt[user_id] = [[software_name, brief, len(pics) + 1]]
            pics.append(pic)
        # print(reuslt)
        data = FormatText("software.txt", start_time, reuslt, "software")
        getAllpic(start_time, pics)
        reponse.code = 200
        reponse.data = data
        return reponse
    else:
        print(f"数据获取失败")

# 获取图片
def getAllpic(dirname:str, pics: list):
    folder_path = f"./pics/{dirname}"
    # https://appstore.api.lazycat.cloud/api/v2/admin/public/d8586f96-2ecf-484a-af0f-9c13545141f9.png
    pic_url = "https://appstore.api.lazycat.cloud/api/v2/admin"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f'文件夹已创建: {folder_path}')
    else:
        print(f'文件夹已存在: {folder_path}')

    for i in range(len(pics)):
        intact_url = pic_url + pics[i]
        print(intact_url)
        response = requests.get(intact_url)
        filename = f"{folder_path}/{i + 1}.png"
        if (response.status_code == 200):
            with open(f'{filename}', 'wb') as f:
                f.write(response.content)
            print('图片下载完成')
        else:
            print(f'下载失败，状态码: {response.status_code}')
