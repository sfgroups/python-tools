from fastapi import FastAPI
from typing import List
from dataclasses import dataclass

app = FastAPI()

@dataclass
class Item:
    name: str
    description: str

@dataclass
class ResponseData:
    items: List[Item]

@app.get("/get_data", response_model=ResponseData)
def get_data():
    # Sample data
    items_data = [
        {"name": "item1", "description": "Description 1"},
        {"name": "item2", "description": "Description 2"}
    ]

    # Create a list of Item objects from the JSON data
    items = [Item(**item_data) for item_data in items_data]

    # Create ResponseData object with the list of items
    response_data = ResponseData(items=items)

    return response_data
