import httpx

from app.core.config import settings

class WhatsappService:
    async def send_text(self,phone_number: str,message: str):
        url = (
            f"https://graph.facebook.com/"
            f"{settings.GRAPH_API_VERSION}/"
            f"{settings.PHONE_NUMBER_ID}/messages"
        )

        headers = {
            "Authorization" : f"Bearer {settings.META_ACCESS_TOKEN}",
            "content-Type" : "application/json",
        }

        payload = {
            "messaging_product" : "whatsapp",
            "to" : phone_number,
            "type" : "text",
            "text" : {
                "body" : message
            },
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                url,
                headers=headers,
                json=payload
            )

        print("status:",response.status_code)
        print(response.text)

        return response    