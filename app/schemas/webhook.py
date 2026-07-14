from pydantic import BaseModel 
from typing import Literal

class IncomingMessage(BaseModel):
    phone_number: str
    message: str
    message_type: Literal["text"]
    message_id: str 
    timestamp: int 

