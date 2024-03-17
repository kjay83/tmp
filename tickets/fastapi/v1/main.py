from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()


from pydantic import BaseModel
from typing import Dict

class Category(BaseModel):
    name: str
    description: str
    sequence: int
    increment: int

class FakeDB:
    def __init__(self):
        self.data: Dict[str, Category] = {}
    def get_category(self, name: str) -> Category:
        return self.data.get(name)
    def add_category(self, name1: str, desc1: str, seq1: str, inc1: str) -> None:
        new_category = Category(name=name1, description=desc1,sequence=seq1,increment=inc1)
        self.data[name1]=new_category
        # self.dat

db = FakeDB()
db.data = {
    "U": Category(name="U",description="default categ", 
                  sequence=1, 
                  increment=1)
}

@app.get('/')
def home():
    return {"message":"Welcome to newtickets app in DEV by jk"}

@app.get("/categories/{name}", response_model=Category)
def read_category(name: str):
    result = db.get_category(name)
    if result == None:
        raise HTTPException(status_code=404, detail=f"Category {name} not found")
    else:
        return result

#create a category jusqe using the namen, with deafult values
@app.post("/categories/{name}", response_model=Category, status_code=201)
def post_category(name: str):
    result = db.get_category(name)
    if result == None:
        db.add_category(name,"deafult description",1,1)
        # response.status_code = status.HTTP_201_CREATED
        return db.get_category(name)
    else:
        raise HTTPException(status_code=403, detail=f"Category {name} aready exist")


@app.get("/newtickets")
def generateDefaultTicket():    
    categ = db.get_category("U")
    if categ == None:
        raise HTTPException(status_code=404, detail="Critical Error! Default category (U) not found")
    else:
        result = "U"+"-"+f"{categ.sequence:04}"
        categ.sequence+=categ.increment
        return result

@app.get("/newtickets/{name}")
def generateTicket(name: str):    
    categ = db.get_category(name)
    if categ == None:
        raise HTTPException(status_code=404, detail=f"Category {name} not found. Please create it first")
    else:
        result = name+"-"+f"{categ.sequence:04}"
        categ.sequence+=categ.increment
        return result
    
if __name__ == "__main__":
    uvicorn.run("main:app",host='0.0.0.0',port=5000,reload=True)