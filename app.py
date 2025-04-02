from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://my-mongodb:27017/")
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
