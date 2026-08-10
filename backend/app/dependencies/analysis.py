"""
Analysis service dependency.
"""

from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.database import get_db
from app.services.analysis_service import AnalysisService


def get_analysis_service(
    db: Session = Depends(get_db),
) -> AnalysisService:
    return AnalysisService(db)
