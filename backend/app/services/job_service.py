"""
Job business service.
"""

from sqlalchemy.orm import Session

from app.models.job import Job
from app.schemas.job import JobCreate


class JobService:
    def __init__(self, db: Session):
        self.db = db

    def create_job(self, job: JobCreate) -> Job:
        db_job = Job(**job.model_dump())

        self.db.add(db_job)
        self.db.commit()
        self.db.refresh(db_job)

        return db_job

    def get_job(self, job_id: int):
        return (
            self.db.query(Job)
            .filter(Job.id == job_id)
            .first()
        )

    def list_jobs(self):
        return self.db.query(Job).all()
