"""示例Pydantic模型"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ExampleBase(BaseModel):
    """基础模型"""
    name: str
    description: Optional[str] = None
    is_active: bool = True


class ExampleCreate(ExampleBase):
    """创建模型"""
    pass


class ExampleUpdate(BaseModel):
    """更新模型"""
    name: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ExampleInDB(ExampleBase):
    """数据库模型"""
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)


class Example(ExampleInDB):
    """返回模型"""
    pass
