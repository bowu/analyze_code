import os, openai
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from commands import handle_message

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    content: str
    role: str

class ChatRequest(BaseModel):
    model: str
    messages: List[Message]
    key: str


@app.post("/api/chat")
async def handle_chat(request: ChatRequest):
    model = request.model
    messages = request.messages
    key = request.key

    openai.api_key = os.getenv("OPENAI_API_KEY")

    message = messages[0].content
    response = await handle_message(message, model)
    return Response(content=response)
