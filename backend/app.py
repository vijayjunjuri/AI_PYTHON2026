from fastapi import FastAPI
from pydantic import BaseModel
from app.banking_chatbot import chatbot
from fastapi.responses import JSONResponse



app = FastAPI()

class ChatRequest(BaseModel):
    query:str


@app.get("/AI")
def status():
    return{
        "message" : "Banking chatbot is running"
    }

# GET http://127.0.0.1:8000/AI


@app.post("/chat")
def chat(request: ChatRequest):
    response = chatbot(request.query)

    return JSONResponse({
        "response" : response
    })


# uvicorn backend.app:app --reload

# http://127.0.0.1:8000
# end points - /AI, /chat