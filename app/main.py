from fastapi import FastAPI
from pydantic import BaseModel

import requests

app = FastAPI()

user_name = None


@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2023&month=12&metroCd=11&cityCd=12&apiKey=FaQvGnHYNQ7GSW7371cu3E6McUG3sF43OxzIKs09&returnType=json"
    
    contents = requests.get(URL).text

    return { "message": contents}

@app.get("/home")
def home():
    return { "message": "Home!" }

'''
@app.post("/user")
def create_item(new_name):
    global user_name
    user_name = new_name
    return { "message": f"Your name is {user_name}!"}

@app.get("/user")
def get_item():
    return {"message": f"Hey, your name is {user_name}!"}

@app.put("/user")
def update_item(update_name):
    global user_name
    user_name = update_name
    return {"message": f"Your name is now {user_name}!"}

@app.delete("/user")
def delete_item():
    user_name = None
    return {"message" : "User name deleted"}
'''