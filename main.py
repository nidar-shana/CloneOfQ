from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "Q Clone is running!"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=request.message
    )

    return {
        "answer": response.output_text
    }
