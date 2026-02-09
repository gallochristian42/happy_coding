"""API依赖项"""

from typing import Generator
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.database import get_db


# 示例：获取当前用户依赖
# async def get_current_user(
#     token: str = Depends(oauth2_scheme),
#     db: Session = Depends(get_db)
# ):
#     """获取当前用户"""
#     # 实现JWT验证逻辑
#     pass


# 示例：管理员权限验证
# async def get_current_admin_user(
#     current_user = Depends(get_current_user),
# ):
#     """验证是否为管理员"""
#     if not current_user.is_admin:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN,
#             detail="Not enough permissions"
#         )
#     return current_user
