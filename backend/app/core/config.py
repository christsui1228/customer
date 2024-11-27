from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Customer Management System"
    DATABASE_URL: str  # 这里没有默认值，意味着必须在环境变量或.env文件中提供

    # 使用 SettingsConfigDict 配置模型
    model_config = SettingsConfigDict(env_file=".env")

@lru_cache()  # 缓存装饰器，避免重复读取环境变量
def get_settings():
    return Settings()

settings = get_settings()