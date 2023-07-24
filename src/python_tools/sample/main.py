# main.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import DatabaseSingleton, SessionLocal
from . import service, models

app = FastAPI()

# Dependency to get the database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# API Endpoint to create an item
@app.post("/items/", response_model=models.Item)
def create_item(name: str, description: str, db: Session = Depends(get_db)):
    item_service = service.ItemService(db)
    return item_service.create_item(name, description)

# API Endpoint to get an item
@app.get("/items/{item_id}", response_model=models.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    item_service = service.ItemService(db)
    item = item_service.get_item(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# API Endpoint to get a list of items
@app.get("/items/", response_model=list[models.Item])
def get_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    item_service = service.ItemService(db)
    return item_service.get_items(skip, limit)
