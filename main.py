from fastapi import FastAPI, Response, status
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def hello():
    return {"/rating/username","/repositories/username"}


@app.get("/rating")
def rating(username: str = ""):
    return {"userWWname"}

@app.get("/repositories")
def list_repo(username: str = ""):
    return {"repositories"}
