from pydantic import BaseModel

class UploadResult(BaseModel):
    original_filename: str
    stored_filename: str
    file_path: str
    media_id: str
    mime_type: str