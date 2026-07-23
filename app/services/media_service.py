import httpx
from pathlib import Path
from app.core.config import settings


class MediaService:
    async def download_pdf(self,media_url: str,filename: str)->str:
        uploads_dir = Path("storage/uploads")
        uploads_dir.mkdir(exist_ok=True)

        file_path = uploads_dir /filename
        headers = {
            "Authorization": f"Bearer {settings.META_ACCESS_TOKEN}"
        }

        async with httpx.AsyncClient(timeout=60) as cilent:
                response = await cilent.get(
                    media_url,
                    headers=headers
                )

                response.raise_for_status()

        with open(file_path,"wb") as f:
             f.write(response.content)

        return str(file_path)             
            