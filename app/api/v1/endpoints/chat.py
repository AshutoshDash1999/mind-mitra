from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.services.chatbot import get_ai_response
from app.services.auth import get_current_user
from app.models.user import User

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

router = APIRouter()

@router.post('/chat', summary="Send chat message to AI", response_model=ChatResponse, openapi_examples={
    "example1": {
        "description": "Send a chat message to AI",
        "value": {
            "message": "I'm feeling anxious about my upcoming presentation"
        }
    }
})
def chat_endpoint(request: ChatRequest, current_user: User = Depends(get_current_user)):
    """Send a chat message to the AI chatbot and return a generated response.

    Request model: 'ChatRequest'
    message: string

    Response model: 'ChatResponse'
    response: string
    """
    ai_response = get_ai_response(request.message)
    return ChatResponse(response=ai_response)