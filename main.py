#python -m uvicorn main:app --reload
#pip install -r path/to/requirements.txt
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def first_api():
    return {"message" :"Hello"}
