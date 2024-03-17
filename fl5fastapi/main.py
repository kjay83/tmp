from fastapi import FastAPI, HTTPException
from flask import abort

app = FastAPI()


from pydantic import BaseModel
from typing import Dict

class Book(BaseModel):
    id: int
    title: str
    author: str
    availability: bool

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Book] = {}
    def get_book(self, id: int) -> Book:
        return self.data.get(id)

db = FakeDB()
db.data = {
    1: Book(id=1, title="1984", author="George Orwell", availability=True)
}

@app.get("/books/{id}", response_model=Book)
def read_book(id: int):
    result = db.get_book(id)
    if result == None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return result