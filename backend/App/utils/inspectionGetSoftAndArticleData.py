# 获取数据加载状态
from getArticleData import GetArticleData
from getSoftwareData import GetContent
from struc.dataLoadStatus import Get_sortware_and_article_data_status


async def InspectDataExists(curTime: str, tomorrow: str): 
    dataLoadingStatus = await Get_sortware_and_article_data_status()
    if (dataLoadingStatus == 0):
        try:
            await GetContent(curTime, tomorrow)
            await GetArticleData(curTime, tomorrow)
        except Exception as e:
           raise

    if (dataLoadingStatus == 1):
        try:
            await GetArticleData(curTime, tomorrow)
        except Exception as e:
            raise

    if (dataLoadingStatus == 2):
        try:
            await GetContent(curTime, tomorrow)
        except Exception as e:
            raise
