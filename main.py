from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import gemini

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
    return f"Hello, {name}!"

@app.get("/details/{id}")
def say_details(id: int):
    details = {1: ["sangameshwar", "sale"]}
    detail = details.get(id, "guest")
    return detail

gemini.api_key = "AIzaSyCi-GoXnRJVeb6Di-d-6wT1NWcKH-Khj7M"  # Updated API key

@app.get("/ask/{pr}")
def ask(pr: str):
    try:
        response = gemini.Completion.create(
            query=pr,
            max_tokens=5
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return {"error": str(e)}
