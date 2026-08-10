"""
Pydantic schemas for AI Analysis.
"""

from typing import Optional

from app.schemas.base import BaseSchema


class AnalysisBase(BaseSchema):
    candidate_id: int
    job_id: int
    resume_id: int

    match_score: Optional[float] = None

    matched_skills: Optional[str] = None
    missing_skills: Optional[str] = None

    strengths: Optional[str] = None
    weaknesses: Optional[str] = None

    recruiter_notes: Optional[str] = None
    ai_recommendation: Optional[str] = None


class AnalysisCreate(AnalysisBase):
    pass


class AnalysisUpdate(BaseSchema):
    match_score: Optional[float] = None
    matched_skills: Optional[str] = None
    missing_skills: Optional[str] = None
    strengths: Optional[str] = None
    weaknesses: Optional[str] = None
    recruiter_notes: Optional[str] = None
    ai_recommendation: Optional[str] = None


class AnalysisResponse(AnalysisBase):
    id: int
