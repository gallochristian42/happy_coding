"""应用配置"""

from typing import List
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """应用配置"""

    # 项目基本信息
    PROJECT_NAME: str = "Happy Coding API"
    VERSION: str = "0.1.0"
    DESCRIPTION: str = "A FastAPI project template"
    
    # 服务器配置
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    DEBUG: bool = True
    
    # API配置
    API_V1_PREFIX: str = "/api/v1"
    
    # 跨域配置
    ALLOWED_HOSTS: List[str] = ["*"]
    
    # 数据库配置
    DATABASE_URL: str = "sqlite:///./happy_coding.db"
    # DATABASE_URL: str = "postgresql://user:password@localhost:5432/dbname"
    
    # Redis配置
    # REDIS_URL: str = "redis://localhost:6379/0"
    
    # JWT配置
    SECRET_KEY: str = "your-secret-key-here-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="allow"
    )


settings = Settings()
