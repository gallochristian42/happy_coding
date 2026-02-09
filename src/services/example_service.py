"""示例服务"""

from typing import Optional, List
from sqlalchemy.orm import Session

from models.example import ExampleModel
from schemas.example import ExampleCreate, ExampleUpdate


class ExampleService:
    """示例服务类"""
    
    @staticmethod
    def get_by_id(db: Session, item_id: int) -> Optional[ExampleModel]:
        """根据ID获取"""
        return db.query(ExampleModel).filter(ExampleModel.id == item_id).first()
    
    @staticmethod
    def get_list(
        db: Session,
        skip: int = 0,
        limit: int = 100
    ) -> List[ExampleModel]:
        """获取列表"""
        return db.query(ExampleModel).offset(skip).limit(limit).all()
    
    @staticmethod
    def create(db: Session, item: ExampleCreate) -> ExampleModel:
        """创建"""
        db_item = ExampleModel(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def update(
        db: Session,
        item_id: int,
        item: ExampleUpdate
    ) -> Optional[ExampleModel]:
        """更新"""
        db_item = ExampleService.get_by_id(db, item_id)
        if not db_item:
            return None
        
        update_data = item.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_item, field, value)
        
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def delete(db: Session, item_id: int) -> bool:
        """删除"""
        db_item = ExampleService.get_by_id(db, item_id)
        if not db_item:
            return False
        
        db.delete(db_item)
        db.commit()
        return True
