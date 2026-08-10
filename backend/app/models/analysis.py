"""
AI analysis database model.
"""

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, Text
from sqlalchemy.sql import func

from app.models.base import Base


class Analysis(Base):
    __tablename__ = "analyses"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    job_id = Column(
        Integer,
        ForeignKey("jobs.id"),
        nullable=False,
    )

    resume_id = Column(
        Integer,
        ForeignKey("resumes.id"),
        nullable=False,
    )

    match_score = Column(Float)

    matched_skills = Column(Text)

    missing_skills = Column(Text)

    strengths = Column(Text)

    weaknesses = Column(Text)

    recruiter_notes = Column(Text)

    ai_recommendation = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
