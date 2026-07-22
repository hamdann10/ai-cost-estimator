from app.schemas.webhook import IncomingMessage
from app.services.whatsapp_service import WhatsappService

class ConversationService:

    async def handle(self,incoming: IncomingMessage):

        print("="*50)
        print("Incomming Message")
        print("="*50)

        await WhatsappService().send_text(
            phone_number=incoming.phone_number,
            message=(
                "Welcome to AI Cost Estimator!\n\n"
                "Please send your Architectural drawing(PDF)"
            ),

        )