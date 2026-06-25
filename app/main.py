from fastapi import FastAPI
from app.routes.project import router as project_router

app = FastAPI()

app.include_router(project_router)

@app.get("/health")
def health():
    return {"status": "running"}


