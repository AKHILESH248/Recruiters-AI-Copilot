"""
Candidate service dependency.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.services.candidate_service import CandidateService


def get_candidate_service(
    db: Session = Depends(get_db),
) -> CandidateService:
    return CandidateService(db)
