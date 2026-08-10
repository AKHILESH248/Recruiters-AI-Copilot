"""
Job service dependency.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.services.job_service import JobService


def get_job_service(
    db: Session = Depends(get_db),
) -> JobService:
    return JobService(db)
