from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from twilio.rest import Client

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://merry-torrone-279def.netlify.app"],  # Specific origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def alert():
    account_sid = "ACd0820c8fb546c38be1760536009548cc"
    auth_token = "a07946d79b75d7a24937ba7ffcf5f083"
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml='<Response><Say>You are receiving this call because there has been a suspicious entry at the door please be alerted</Say></Response>',
        to='+918247341184',
        from_='+15856693126'
    )
    print("Alert sent")

@app.get("/")
def read_root():
    return "Welcome to FastAPI!"

@app.get("/hello/{id}")
def say_hello_by_id(id: int):
    greetings = {1: "Sangameshwar", 2: "Rithik", 3: "Santhosh"}
    name = greetings.get(id, "Guest")
    if id == 1:
        alert()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if 5 <= now.hour < 12:
        time_of_day = "morning"
    elif 12 <= now.hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"
    return f"Hello, {name}! It is currently {current_time}, {time_of_day}."
