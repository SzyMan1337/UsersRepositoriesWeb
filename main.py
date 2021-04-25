from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return{"username","username/rate"}