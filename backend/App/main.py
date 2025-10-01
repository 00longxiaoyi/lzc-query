from datetime import datetime, timedelta
import os
from os.path import dirname
from fastapi import Body, FastAPI, WebSocket
from fastapi.responses import FileResponse
from getArticleData import GetArticleData
from getArticlePendingData import GetArticlePengdingData
from getSoftwareData import GetContent
from getSoftwarePendingData import GetSoftwarePendingData
from struc.websocksType import WsSendJsonInfo
from tokenOperation import GetTokenInfo, SetTokenInfo
from utils.GetImages import GetALlPicZip, GetAllpic
from utils.Token import getToken, initToken

from fastapi.middleware.cors import CORSMiddleware

from utils.data import get_pic_data

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
    #curTime = "2025-09-28"
    #tomorrow = "2025-09-29"    
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return await GetContent(str(curTime), str(tomorrow))
    #return GetContent("2025-09-05", "2025-09-06")

@app.get("/get_soft_ware_pending_data")
def getSoftWarePendingDataRoute():
    return GetSoftwarePendingData() 

@app.get("/get_article_pending_data")
def getArticlePendingDataRoute():
    return GetArticlePengdingData()

@app.get("/get_article_data")
def getArticleDataRoute():
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return GetArticleData(str(curTime), str(tomorrow))
    #return GetArticleData("2025-09-05", "2025-09-06")

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
            data="websocket连接失败"
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port= 8080,
        reload=True
    )
