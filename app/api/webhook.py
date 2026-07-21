from fastapi import APIRouter,Request
from fastapi.responses import PlainTextResponse
import json
from app.core.config import settings
from app.schemas.webhook import IncomingMessage
from app.services.conversation_service import ConversationService


router = APIRouter(prefix="/webhook",tags=["WhatsApp"])

@router.get("")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")
    print("Mode:", mode)
    print("Meta Token:", token)
    print("App Token :", settings.VERIFY_TOKEN)

    if mode == "subscribe" and token == settings.VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)
    
    return PlainTextResponse("Veritification failed",status_code=403)

@router.post("")
async def receive_webhook(request: Request):
    body = await request.json()

    print("=" * 80)
    print(json.dumps(body, indent=2))
    print("=" * 80)

    value = body["entry"][0]["changes"][0]["value"]

    if "messages" in value:

      message = value["messages"][0]

      incoming = IncomingMessage(
        phone_number=message["from"],
        message=message["text"]["body"],
        message_type=message["type"],
        message_id=message["id"],
        timestamp=int(message["timestamp"]),
    )

      await ConversationService().handle(incoming)

    return {"status": "received"}
