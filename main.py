# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World 2"}

@app.get("/items/{item_id}")
async def read_item(item_id: bool):
    return {"item_id": item_id}