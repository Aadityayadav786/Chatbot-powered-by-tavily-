from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

ALLOWED_MODEL_NAMES = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]

app = FastAPI(title="LangGraph AI Agent")

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Select a valid AI model."}

    response = get_response_from_ai_agent(
        request.model_name, request.messages[0], request.allow_search, request.system_prompt, request.model_provider
    )
    
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)
