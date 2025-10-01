import os
import asyncio
import aiohttp
import zipfile
from typing import List
from fastapi import WebSocket

from struc.responseStruc import ResponseStruc
from struc.software import TempPicInfoStruc
from struc.websocksType import WsSendJsonInfo

async def download_pic(
        session: aiohttp.ClientSession, 
        folder_path: str, 
        base_url: str, 
        pic: TempPicInfoStruc, 
        websockt: WebSocket, 
        retries: int = 3,
        timeout: int = 10
) -> dict:
    """ 异步下载图片 并支持 ws实时通知
    Args:
        session     aiohttp.ClientSession 
        folder_path str: 文件夹路径
        base_url    str: 图片路径
        pic         str: 图片数据
        websockt    WebSocket: ws字节套
        retries     int: 重试次数
        timeout     int: 超时时间
    Returns:
        return type: description
    """

    intact_url = base_url + pic.url
    filename = f"{folder_path}/{pic.name}.png"
    for i in range(retries):
        try:
            async with session.get(intact_url, timeout=aiohttp.ClientTimeout(retries * timeout)) as response:
                if response.status == 200:
                    content = await response.read()
                    with open(filename, "wb") as f:
                        f.write(content)

                    await websockt.send_json(WsSendJsonInfo(
                        type="success",
                        data=f"{pic.name} 图片下载成功"
                    ).__dict__)
                    return {"name": pic.name, "status": "success", "path": filename}
                else:
                    return {"name": pic.name, "status": f"failed({response.status})"}

        except asyncio.TimeoutError as e:
            await websockt.send_json(WsSendJsonInfo(
                type="error",
                data=f"{pic.name} 图片下载超时"
            ).__dict__)
            raise e

        except Exception as e:
            await websockt.send_json(WsSendJsonInfo(
                type="error",
                data=f"{pic.name} 图片下载失败"
            ).__dict__)
            raise e

    await websockt.send_json(WsSendJsonInfo(
                type="error",
                data=f"{pic.name} 图片下载失败"
            ).__dict__)
    return {"name": pic.name, "status": f"error"}

async def GetAllpic(dirname: str, pics: List[TempPicInfoStruc], websockt: WebSocket):
    """异步获取图片信息并通过wc返回给前端消息"""

    folder_path = f"./files/pics/{dirname}"
    base_url = "https://appstore.api.lazycat.cloud/api/v2/admin"

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹已创建: {folder_path}")
    else:
        print(f"文件夹已存在: {folder_path}")

    async with aiohttp.ClientSession() as session:
        tasks = [download_pic(session, folder_path, base_url, pic, websockt) for pic in pics]
        await asyncio.gather(*tasks)
        await websockt.send_json(WsSendJsonInfo(
                type="warning",
                data=f"图片已全部下载，可以下载图片压缩包了"
            ).__dict__)

async def createZipfile(dirname: str, zipname: str):
    """获取图片压缩包数据
    Args:
        dirname str: 目录名称
        zipname str: 压缩包名称
    """
    picPath = f"./files/pics/{dirname}"
    zipPath = f"./files/zips/{zipname}.zip"
    if not os.path.exists("./files/zips"):
        os.mkdir("./files/zips/")
    try:
        with zipfile.ZipFile(zipPath, "w", zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(picPath):
                for file in files:
                    filePath = os.path.join(root, file)
                    arcname = os.path.relpath(filePath, picPath)  # 保持目录结构
                    zipf.write(filePath, arcname)

    except Exception as e:
        raise e

async def GetALlPicZip(dirname: str):
    """ 获取所有照片的接口 """  
    result = ResponseStruc()
    try:
        result.code = 200
        # 获取压缩包  
        await createZipfile(dirname, dirname)
        result.data = {
            "zip_name": f"{dirname}.zip"
        }
        return result 
    except Exception as e:
        result.error = str(e)
        result.code = 500
