"""
Candidate business service.
"""

from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate


class CandidateService:
    def __init__(self, db: Session):
        self.db = db

    def create_candidate(self, candidate: CandidateCreate) -> Candidate:
        db_candidate = Candidate(**candidate.model_dump())

        self.db.add(db_candidate)
        self.db.commit()
        self.db.refresh(db_candidate)

        return db_candidate

    def get_candidate(self, candidate_id: int):
        return (
            self.db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )

    def list_candidates(self):
        return self.db.query(Candidate).all()
