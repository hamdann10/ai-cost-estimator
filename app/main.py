from fastapi import FastAPI

from app.api.health import router as health_router
from app.core.config import settings
from app.api.webhook import router as webhook_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,

)

app.include_router(health_router)
app.include_router(webhook_router)

@app.get("/")
def root():
    return{
        "message": "AI Construction Estimation API",
        "version": settings.APP_VERSION,
        "status": "running"
    }