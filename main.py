from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai

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

openai.api_key = "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"

@app.get("/ask/{pr}")
def ask(pr: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": pr}
            ]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return {"error": str(e)}
