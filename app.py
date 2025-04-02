import os
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Get MongoDB URL from environment variable (or use default)
mongo_url = os.getenv("MONGO_URL", "mongodb://my-mongodb:27017/")
# Connect to MongoDB
client = MongoClient(mongo_url)
db = client["testdb"]
collection = db["items"]

@app.post("/add")
async def add_item(name: str):
    collection.insert_one({"name": name})
    return {"message": "Item added", "name": name}

@app.get("/items")
async def get_items():
    items = list(collection.find({}, {"_id": 0}))
    return {"items": items}

@app.get("/")
async def root():
    return {"message": "FastAPI is running OK!"}
