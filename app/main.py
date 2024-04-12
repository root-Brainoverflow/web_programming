from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_name = None

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