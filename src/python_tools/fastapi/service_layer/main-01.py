# main.py

from fastapi import FastAPI
from .config import SingletonConfig

app = FastAPI()
config = SingletonConfig()

# Use the config values
database_url = config.database_url
max_items_per_page = config.max_items_per_page

# API Endpoint
@app.get("/items/")
def get_items():
    # Your API logic here...
    return {"message": "Items endpoint"}
