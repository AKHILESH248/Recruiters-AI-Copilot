"""
Resume API routes.
"""

from fastapi import APIRouter, Depends

from app.dependencies.resume import get_resume_service
from app.schemas.resume import ResumeCreate
from app.services.resume_service import ResumeService

router = APIRouter(
    prefix="/resumes",
    tags=["Resumes"],
)


@router.get("/")
def list_resumes(
    service: ResumeService = Depends(get_resume_service),
):
    return service.list_resumes()


@router.get("/{resume_id}")
def get_resume(
    resume_id: int,
    service: ResumeService = Depends(get_resume_service),
):
    return service.get_resume(resume_id)


@router.post("/")
def create_resume(
    resume: ResumeCreate,
    service: ResumeService = Depends(get_resume_service),
):
    return service.create_resume(resume)
