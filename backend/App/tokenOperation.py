from configparser import Error
from struc.responseStruc import ResponseStruc
from utils.Token import getToken, setToken


def GetTokenInfo():
    result = ResponseStruc()
    token = getToken()

    if (token != ""):
        result.code = 200
        result.data = token

    return result


def SetTokenInfo(token: str):
    result = ResponseStruc()
    if (token == ""):
        result.code = 400
        result.error = "token不能空"
        return result
    try:
        setToken(token)
        r_token = getToken()
        result.code = 200
        result.data = r_token
    except Error as e:
        result.error = str(e)

    return result


