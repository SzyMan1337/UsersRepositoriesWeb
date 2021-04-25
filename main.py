from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/")
def hello():
    return {"List all user repositories with ratings": "/repositories?username", "Display sum of all user's repositories ratings":"/rating?username"}

def get_json_of_user(username):
    response = requests.get('https://api.github.com/users/'+username+'/repos')
    if response.ok:
        repo_json = response.json()
        return repo_json, True
    
    return {}, False

@app.get("/rating")
def rating(username: str = ""):
    repo_json,status = get_json_of_user(username)
    if status:
        count = 0
        for i in range(0,len(repo_json)):
            count += repo_json[i]['stargazers_count']
        return {"rating": count}
    return {"Incorrect username": f"{username}"}

@app.get("/repositories")
def list_repo(username: str = ""):
    repo_json,status = get_json_of_user(username)
    if status:
        jss = {}
        for i in range(0,len(repo_json)):
            jss[repo_json[i]['name']] = repo_json[i]['stargazers_count']
        return jss
    return {"Incorrect username": f"{username}"}

