from struc.picData import get_pic_data
from struc.responseStruc import ResponseStruc

async def GetAllPicNum() -> ResponseStruc:
    """返回所有图片的数量
    Returns:
       ResponseStruc: 结果 
    """
    result = ResponseStruc(
        code=200
    )
    num = 0
    try:
        num = await get_pic_data()
        result.data = {
            "num": len(num)
        } 
    except Exception as e:
        result.code = 500
        result.error = str(e) 

    return result
