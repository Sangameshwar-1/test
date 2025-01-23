from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from twilio.rest import Client
import requests

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific domains for better security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Twilio configuration
TWILIO_ACCOUNT_SID = "ACd0820c8fb546c38be1760536009548cc"
TWILIO_AUTH_TOKEN = "a07946d79b75d7a24937ba7ffcf5f083"
TWILIO_PHONE_NUMBER = "+15856693126"

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Base URL for Gemini API
GEMINI_BASE_URL = "https://api.gemini.com/v1"

class CallRequest(BaseModel):
    to: str
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/hello/{id}")
def say_hello_by_id(id: int):
    greetings = {1: "Sangameshwar", 2: "Rithik", 3: "Santhosh"}
    name = greetings.get(id, "Guest")
    return {"message": f"Hello, {name}!"}

@app.get("/details/{id}")
def say_details(id: int):
    details = {
        1: {"name": "Sangameshwar", "role": "Sale"},
        2: {"name": "Rithik", "role": "Developer"},
        3: {"name": "Santhosh", "role": "Manager"},
    }
    return details.get(id, {"name": "Guest", "role": "Unknown"})

@app.get("/symbols")
def get_symbols():
    """Fetch available trading pairs from Gemini."""
    try:
        response = requests.get(f"{GEMINI_BASE_URL}/symbols")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return {"symbols": response.json()}
    except requests.RequestException as e:
        return {"error": str(e)}

@app.get("/ticker/{symbol}")
def get_ticker(symbol: str):
    """Fetch ticker information for a given trading pair."""
    try:
        response = requests.get(f"{GEMINI_BASE_URL}/pubticker/{symbol}")
        response.raise_for_status()  # Raise an exception for HTTP errors
        return {"ticker": response.json()}
    except requests.RequestException as e:
        return {"error": str(e)}

@app.post("/call")
def make_call(call_request: CallRequest):
    try:
        call = client.calls.create(
            to=+918247341184,
            from_=TWILIO_PHONE_NUMBER,
            twiml=f'<Response><Say>{call_request.message}</Say></Response>'
        )
        return {"sid": call.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
