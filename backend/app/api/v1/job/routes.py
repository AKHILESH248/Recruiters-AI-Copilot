"""
Job API routes.
"""

from fastapi import APIRouter, Depends

from app.dependencies.job import get_job_service
from app.schemas.job import JobCreate
from app.services.job_service import JobService

router = APIRouter(
    prefix="/jobs",
    tags=["Jobs"],
)


@router.get("/")
def list_jobs(
    service: JobService = Depends(get_job_service),
):
    return service.list_jobs()


@router.get("/{job_id}")
def get_job(
    job_id: int,
    service: JobService = Depends(get_job_service),
):
    return service.get_job(job_id)


@router.post("/")
def create_job(
    job: JobCreate,
    service: JobService = Depends(get_job_service),
):
    return service.create_job(job)
