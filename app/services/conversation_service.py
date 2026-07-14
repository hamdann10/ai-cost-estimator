from app.schemas.webhook import IncomingMessage

class ConversationService:

    def handle(self,incoming: IncomingMessage):

        print("="*50)
        print("Incomming Message")
        print("="*50)

        print(f"Phone  : {incoming.phone_number}")
        print(f"Message  : {incoming.message}")
        print(f"Type  : {incoming.message_type}")
        print(f"Message ID  : {incoming.message_id}")
        print(f"Timestamp  : {incoming.timestamp}")