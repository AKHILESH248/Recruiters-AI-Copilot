"""
Job database model.
"""

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.models.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    job_title = Column(String(255), nullable=False)

    client_name = Column(String(255))

    job_location = Column(String(255))

    employment_type = Column(String(100))

    experience_required = Column(String(100))

    salary_range = Column(String(100))

    job_description = Column(Text, nullable=False)

    required_skills = Column(Text)

    preferred_skills = Column(Text)

    recruiter_name = Column(String(255))

    recruiter_email = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
