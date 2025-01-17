from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{id}")
def say_hello_by_id(id: int):
    greetings = {1: "Sangameshwar",2:"Rithik",3:"santhosh"}
    name = greetings.get(id, "Guest")
    return {"message": f"Hello, {name}!"}
