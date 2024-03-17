from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Gello5 world"}

if __name__ == "__main__":    
    # uvicorn.run("main:app", port=5000, log_level="info",host="0.0.0.0",reload=True)
    uvicorn.run("main:app", port=5000,host="0.0.0.0",reload=True)