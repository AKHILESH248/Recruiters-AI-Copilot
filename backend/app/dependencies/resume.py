"""
Resume service dependency.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.services.resume_service import ResumeService


def get_resume_service(
    db: Session = Depends(get_db),
) -> ResumeService:
    return ResumeService(db)
