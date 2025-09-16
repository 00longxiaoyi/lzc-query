import os
import yaml

configFile = "./config/config.yml"

# 内存缓存 token
_token = None

def _loadConfig():
    """加载 YAML 配置文件"""
    if os.path.exists(configFile):
        with open(configFile, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    else:
        return {}

def _saveConfig(config: dict):
    """写入 YAML 配置文件"""
    with open(configFile, "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True)

def initToken():
    """初始化 Token（文件不存在时从环境变量生成）"""
    global _token
    config = _loadConfig()
    token = config.get("TOKEN")
    if not token:
        token = os.getenv("TOKEN", "")
        config["TOKEN"] = token
        _saveConfig(config)
    _token = token

def getToken():
    """获取 Token"""
    global _token
    if _token is None:
        initToken()
    return _token

def setToken(token: str):
    """更新 Token（同时更新内存和文件）"""
    global _token
    _token = token
    config = _loadConfig()
    config["TOKEN"] = token
    _saveConfig(config)
