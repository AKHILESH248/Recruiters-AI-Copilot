"""
Resume business service.
"""

from sqlalchemy.orm import Session

from app.models.resume import Resume
from app.schemas.resume import ResumeCreate


class ResumeService:
    def __init__(self, db: Session):
        self.db = db

    def create_resume(self, resume: ResumeCreate) -> Resume:
        db_resume = Resume(**resume.model_dump())

        self.db.add(db_resume)
        self.db.commit()
        self.db.refresh(db_resume)

        return db_resume

    def get_resume(self, resume_id: int):
        return (
            self.db.query(Resume)
            .filter(Resume.id == resume_id)
            .first()
        )

    def list_resumes(self):
        return self.db.query(Resume).all()
