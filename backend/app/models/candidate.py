"""
Candidate database model.
"""

from sqlalchemy import Column, DateTime, Integer, String, Text
from sqlalchemy.sql import func

from app.models.base import Base


class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(255), nullable=False)

    email = Column(String(255), unique=True, index=True)

    phone = Column(String(50))

    location = Column(String(255))

    resume_filename = Column(String(255))

    skills = Column(Text)

    experience_years = Column(Integer)

    current_company = Column(String(255))

    current_title = Column(String(255))

    linkedin_url = Column(String(500))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
