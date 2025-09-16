import requests

DEVUSER_URL = "https://appstore.api.lazycat.cloud/api/v3/admin/developer?sort=-id&page=0&size=20&user_id="

# 获取用户名和群号
def GetDevUserInfo(userID: str):
    HEADERS = {
    "Cookie": "userToken=c2eef5eb015e44589ec77ad6acff2315"
    }
    if (userID == "" or userID is None): return f"用户信息未知， ID为{userID}" 

    res =  requests.get(DEVUSER_URL+userID, headers=HEADERS)
    if (res.status_code == 200):
        if ("items" in  res.json().keys() and len(res.json()["items"]) > 0):
            item_json = res.json()["items"][0]
            remark = ""
            uuid = ""
            if ("remark" in item_json.keys()):
                remark = item_json["remark"]
            if ("other_data" in item_json.keys() and  item_json["other_data"] and "customer_uuid" in item_json["other_data"].keys()):
                uuid = item_json["other_data"]["customer_uuid"]
            return f"{remark}: - {userID} - {uuid}"
        return f"用户信息未知， ID为${userID}"
    return f"用户信息未知， ID为${userID}"
