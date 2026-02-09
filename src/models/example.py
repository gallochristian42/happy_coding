"""示例数据库模型"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func

from config.database import Base


class ExampleModel(Base):
    """示例模型"""
    
    __tablename__ = "examples"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
