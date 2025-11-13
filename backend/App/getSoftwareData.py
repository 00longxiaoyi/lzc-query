""" 获取已审核应用数据 """
from typing import Any, List
import requests
from struc.picData import set_pic_data
from struc.responseStruc import ResponseStruc
from struc.softDataFunc import set_software_data
from struc.software import SoftwareDataStruc, TempPicInfoStruc
from utils.FormatText import FormatTextOfSingleType
from utils.Token import getToken 


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

    pics: List[TempPicInfoStruc] = []
    software_list: List[SoftwareDataStruc] = []
    reponse = ResponseStruc()
    res = requests.get(APP_URL, headers=HEADERS, params=QUERY_CONTENT)
    # print(res.url)
    if (res.status_code == 200):
        res_list = res.json()['items']
        # create_user -> id
        # info_data -> zh -> name
        # info_data -> zh -> screenshot_pc_paths[0]
        for item in res_list:

            user_id = item["create_user"]["id"]
            user_nick_name = item["create_user"]["nickname"]
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

            software_list.append(SoftwareDataStruc(
                id=f"soft_{len(software_list)+1}",
                user_id=user_id,
                nick_name=user_nick_name,
                brief=brief,
                name=software_name
            ))

            if (pic.name and pic.url):
                pics.append(pic)

        #reuslt = mergeResult(software_list)
        data = await FormatTextOfSingleType(software_list)
        # 保存临时图片数据 
        await set_pic_data(pics)
        # 保存应用数据（统计时使用）
        await set_software_data(software_list)

        reponse.code = 200
        reponse.data = data
        return reponse
    else:
        print(f"数据获取失败")


#def mergeResult(data: List[SoftwareDataStruc]) -> dict[Any, Any]:
#    """ 返回格式化需要的数据格式 """
#    result = {}
#    for i in data:
#        if (i.user_id in result.keys()):
#            result[i.user_id].append([i.name, i.brief])
#        else:
#            result[i.user_id] = [[i.name, i.brief]]
#    return result
