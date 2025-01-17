
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

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
    return "Welcome to FastAPI!"

@app.get("/hello/{id}")
def say_hello_by_id(id: int):
    greetings = {1: "Sangameshwar", 2: "Rithik", 3: "Santhosh"}
    name = greetings.get(id, "Guest")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if 5 <= now.hour < 12:
        time_of_day = "morning"
    elif 12 <= now.hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"
    return f"Hello, {name}!{time_of_day}"
