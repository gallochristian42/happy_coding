"""示例端点"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.database import get_db

router = APIRouter()


@router.get("/")
async def list_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """获取列表"""
    return {"items": [], "total": 0}


@router.get("/{item_id}")
async def get_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """获取单个项"""
    return {"id": item_id, "name": "Example Item"}


@router.post("/")
async def create_item(
    # item: ItemCreate,
    db: Session = Depends(get_db)
):
    """创建项"""
    return {"message": "Item created"}


@router.put("/{item_id}")
async def update_item(
    item_id: int,
    # item: ItemUpdate,
    db: Session = Depends(get_db)
):
    """更新项"""
    return {"message": "Item updated"}


@router.delete("/{item_id}")
async def delete_item(
    item_id: int,
    db: Session = Depends(get_db)
):
    """删除项"""
    return {"message": "Item deleted"}
