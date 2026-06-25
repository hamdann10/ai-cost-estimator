from fastapi import APIRouter
from app.models.project import ProjectCreate

router = APIRouter()

@router.get("/projects")
def create_project(project: ProjectCreate):
    return {"message": "Project created",
            "project_name": project.name
            }
