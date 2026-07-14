from fastapi import APIRouter,Request
from fastapi.responses import PlainTextResponse
from app.core.config import settings

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

    print(body)

    return {"status":"received"}
