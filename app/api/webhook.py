from fastapi import APIRouter,Request
from fastapi.responses import PlainTextResponse
from app.core.config import settings
from app.schemas.webhook import IncomingMessage
from app.services.conversation_service import ConversationService

router = APIRouter(prefix="/webhook",tags=["WhatsApp"])

@router.get("")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode == "subscribe" and token == settings.VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)
    
    return PlainTextResponse("Veritification failed",status_code=403)

@router.post("")
async def receive_webhook(request: Request):
    body = await request.json()

    message = body["entry"][0]["changes"][0]["value"]["messages"][0]
    incoming = IncomingMessage(
        phone_number=message["from"],
        message=message["text"]["body"],
        message_type=message["type"],
        message_id=message["id"],
        timestamp=int(message["timestamp"]),
    )

    ConversationService().handle(incoming)
    return {"status":"received"}
