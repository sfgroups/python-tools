# service.py

from sqlalchemy.orm import Session

from . import models


class ItemService:
    def __init__(self, db: Session):
        self.db = db

    def create_item(self, name: str, description: str):
        item = models.Item(name=name, description=description)
        self.db.add(item)
        self.db.commit()
        self.db.refresh(item)
        return item

    def get_item(self, item_id: int):
        return self.db.query(models.Item).filter(models.Item.id == item_id).first()

    def get_items(self, skip: int = 0, limit: int = 10):
        return self.db.query(models.Item).offset(skip).limit(limit).all()
