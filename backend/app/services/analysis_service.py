"""
AI analysis business service.
"""

from sqlalchemy.orm import Session

from app.models.analysis import Analysis
from app.schemas.analysis import AnalysisCreate


class AnalysisService:
    def __init__(self, db: Session):
        self.db = db

    def create_analysis(self, analysis: AnalysisCreate) -> Analysis:
        db_analysis = Analysis(**analysis.model_dump())

        self.db.add(db_analysis)
        self.db.commit()
        self.db.refresh(db_analysis)

        return db_analysis

    def get_analysis(self, analysis_id: int):
        return (
            self.db.query(Analysis)
            .filter(Analysis.id == analysis_id)
            .first()
        )

    def list_analyses(self):
        return self.db.query(Analysis).all()
