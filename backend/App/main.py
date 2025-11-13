from datetime import datetime, timedelta
import os
from typing import List
from fastapi import Body, FastAPI, WebSocket
from fastapi.responses import FileResponse
from getAllPicsNum import GetAllPicNum
from getArticleData import GetArticleData
from getArticlePendingData import GetArticlePengdingData
from getSoftwareData import GetContent
from getSoftwarePendingData import GetSoftwarePendingData
from getSortAndArticleData import GetSortAndArticleData
from getSummaryData import GetSummaryData
from setSortAndArticleData import SetMoneyData
from struc.picData import get_pic_data
from struc.software import CompletedDataStruc
from struc.websocksType import WsSendJsonInfo
from tokenOperation import GetTokenInfo, SetTokenInfo
from utils.GetImages import GetALlPicZip, GetAllpic
from utils.Token import getToken, initToken

from fastapi.middleware.cors import CORSMiddleware

# 初始化一次
initToken()

# 获取 token
token = getToken()

app = FastAPI()


# 允许跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 或者 ["http://localhost:5173"] 前端地址
    allow_credentials=True,
    allow_methods=["*"],   # GET, POST, OPTIONS, PUT, DELETE...
    allow_headers=["*"],   # 自定义 header
)

@app.get("/get_soft_ware_data")
async def getSoftWareDataRoute():
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return await GetContent(str(curTime), str(tomorrow))
    #return await GetContent("2025-09-05", "20215-09-06")

@app.get("/get_soft_ware_pending_data")
def getSoftWarePendingDataRoute():
    return GetSoftwarePendingData() 

@app.get("/get_article_pending_data")
def getArticlePendingDataRoute():
    return GetArticlePengdingData()

@app.get("/get_article_data")
async def getArticleDataRoute():
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return await GetArticleData(str(curTime), str(tomorrow))
    #return await GetArticleData("2025-09-05", "2025-09-06")

@app.get("/get_token")
def getTokenRoute():
    return GetTokenInfo()

@app.post("/set_token")
def setTokenRoute(token: str = Body(..., embed=True)):
    return SetTokenInfo(token)

@app.websocket("/ws/pics_info")
async def wsGetAllPicsInfo(websocket: WebSocket):
    await websocket.accept()
    curTime = datetime.now().date()
    # curTime = "2025-09-28"
    try:
        pics = await get_pic_data()
        await GetAllpic(str(curTime), pics, websocket)
    except Exception as e:
        await websocket.send_json(WsSendJsonInfo(
            type="error",
            data=str(e)
        ).__dict__)

@app.get("/download/zipfile")
async def getZIPContentRoute():
    dirname = str(datetime.now().date())
    # dirname = "2025-09-28"
    await GetALlPicZip(dirname)
    filePath = f"./files/zips/{dirname}.zip"
    print(dirname)
    if not os.path.exists(filePath):
        return {"error": "文件不存在"}
    return FileResponse(
        filePath,
        media_type="application/zip",
        filename=dirname
    )

@app.get("/get_soft_article_data")
async def getSoftArticleDataRoute():
    """ 路由: 应用和文章的表单数据 """
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return await GetSortAndArticleData(str(curTime), str(tomorrow))
    #return await GetSortAndArticleData("2025-09-05", "2025-09-06")


@app.post("/set_soft_article_data")
async def setSoftArticleDataRoute(data: List[CompletedDataStruc] = Body(..., embed=True)):
    """ 路由：设置应用和文章的数据 """
    return await SetMoneyData(data) 


@app.get("/get_soft_article_text_data")
async def getSoftArticleTextDataRoute():
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return await GetSummaryData(str(curTime), str(tomorrow))
    #return await GetSummaryData("2025-09-05", "2025-09-06")

@app.get("/get_all_pics_num")
async def getAllPicsNumRoute():
    return await GetAllPicNum()
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port= 8080,
        reload=True
    )
