from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_name = "WoojinJeon"

@app.post("/user")
def create_item(user: user_name):
    user_name = user.name
    return { "message": f"Your name is {user_name}!"}

@app.get("/user")
def get_item():
    return {"message": f"Hey, your name is {user_name}!"}

@app.put("/user")
def update_item(user: user_name):
    user_name = user.name
    return {"message": f"Your name is now {user_name}!"}

@app.delete("/user")
def delete_item():
    user_name = None
    return {"message" : "User name deleted"}