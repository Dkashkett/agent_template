from fastapi import APIRouter

from app.schemas.message import MessageRequest, MessageResponse
from app.services.agent_service import process_user_message

router = APIRouter()


@router.post("/message", response_model=MessageResponse)
async def handle_message(request: MessageRequest):
    agent_response = await process_user_message(request.user_message)
    return MessageResponse(agent_message=agent_response)
