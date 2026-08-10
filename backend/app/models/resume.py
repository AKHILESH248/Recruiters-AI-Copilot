"""
Resume database model.
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.sql import func

from app.models.base import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        Integer,
        ForeignKey("candidates.id"),
        nullable=False,
    )

    original_filename = Column(String(255), nullable=False)

    stored_filename = Column(String(255), nullable=False)

    file_type = Column(String(50))

    file_size = Column(Integer)

    parsed_text = Column(Text)

    ai_summary = Column(Text)

    upload_status = Column(String(50), default="uploaded")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )
