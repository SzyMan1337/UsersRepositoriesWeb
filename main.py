from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/")
def hello():
    return {"/rating/username","/repositories/username"}

def getJsonOfUser(username):
    request = requests.get('https://api.github.com/users/'+username+'/repos')
    repo_json = request.json()
    return repo_json

@app.get("/rating")
def rating(username: str = ""):
    return {f"rating {username}"}

@app.get("/repositories")
def list_repo(username: str = ""):
    return {"repositories {username}"}
