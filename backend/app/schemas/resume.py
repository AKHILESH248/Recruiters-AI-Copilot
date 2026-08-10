"""
Pydantic schemas for Resume.
"""

from typing import Optional

from app.schemas.base import BaseSchema


class ResumeBase(BaseSchema):
    candidate_id: int
    original_filename: str
    stored_filename: str
    file_type: Optional[str] = None
    file_size: Optional[int] = None
    parsed_text: Optional[str] = None
    ai_summary: Optional[str] = None
    upload_status: Optional[str] = "uploaded"


class ResumeCreate(ResumeBase):
    pass


class ResumeUpdate(BaseSchema):
    parsed_text: Optional[str] = None
    ai_summary: Optional[str] = None
    upload_status: Optional[str] = None


class ResumeResponse(ResumeBase):
    id: int
