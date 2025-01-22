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

openai.api_key = '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'

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
