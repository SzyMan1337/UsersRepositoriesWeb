from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/")
def hello():
    return {"List all user repositories with ratings": "/repositories/username", "Display sum of all user's repositories ratings":"/rating/username"}

def get_json_of_user(username):
    request = requests.get('https://api.github.com/users/'+username+'/repos')
    repo_json = request.json()
    return repo_json

@app.get("/rating")
def rating(username: str = ""):
    repo_json = get_json_of_user(username)
    count = 0
    for i in range(0,len(repo_json)):
        count += repo_json[i]['stargazers_count']
    return {"rating": count}

@app.get("/repositories")
def list_repo(username: str = ""):
    repo_json = get_json_of_user(username)
    jss = {}
    for i in range(0,len(repo_json)):
        jss[repo_json[i]['name']] = repo_json[i]['stargazers_count']
    return jss
