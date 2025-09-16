from datetime import datetime, timedelta
from fastapi import Body, FastAPI
from getArticleData import GetArticleData
from getArticlePendingData import GetArticlePengdingData
from getSoftwareData import GetContent
from getSoftwarePendingData import GetSoftwarePendingData
from tokenOperation import GetTokenInfo, SetTokenInfo
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
def getSoftWareDataRoute():
    curTime = datetime.now().date()
    tomorrow = curTime + timedelta(days=1)
    return GetContent(str(curTime), str(tomorrow))
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port= 8080,
        reload=True
    )
