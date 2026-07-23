from app.schemas.upload import UploadResult
from uuid import uuid4
from pathlib import Path
from app.services.media_service import MediaService

class UploadService:
    async def process_document(self,document:dict)-> UploadResult:
        """
        Process of Uploaded Whatsapp document.

        steps:
        1.Read document metadata
        2.Generate unique filename
        3.Download and save the file
        4.Return upload information
         
        """
        original_filename = document["filename"]
        mime_type = document["mime_type"]
        media_id = document["id"]
        media_url = document["url"]

        extension = Path(original_filename).suffix

        stored_filename = f"{uuid4()}{extension}"

        file_path = await MediaService().download_pdf(
            media_url=media_url,
            filename=stored_filename
        )

        return UploadResult(
             original_filename = original_filename,
             stored_filename = stored_filename,
             file_path = file_path,
             media_id = media_id,
             mime_type = mime_type
        )