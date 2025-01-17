
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your domain if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{id}")
def say_hello_by_id(id: int):
    greetings = {1: "Sangameshwar", 2: "Rithik", 3: "Santhosh"}
    name = greetings.get(id, "Guest")
    return {"message": f"Hello, {name}!"}
