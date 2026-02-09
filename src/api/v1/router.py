"""API v1路由汇总"""

from fastapi import APIRouter

# 导入各个端点路由
# from .endpoints import users, items, auth

api_router = APIRouter()

# 注册各个模块的路由
# api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])


# 示例端点
@api_router.get("/example")
async def example():
    """示例端点"""
    return {"message": "This is an example endpoint"}
