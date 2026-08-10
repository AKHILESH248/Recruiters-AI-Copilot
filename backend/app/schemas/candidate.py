"""
Pydantic schemas for Candidate.
"""

from typing import Optional

from pydantic import EmailStr

from app.schemas.base import BaseSchema


class CandidateBase(BaseSchema):
    full_name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    current_company: Optional[str] = None
    current_title: Optional[str] = None
    experience_years: Optional[int] = None
    linkedin_url: Optional[str] = None


class CandidateCreate(CandidateBase):
    pass


class CandidateUpdate(BaseSchema):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    current_company: Optional[str] = None
    current_title: Optional[str] = None
    experience_years: Optional[int] = None
    linkedin_url: Optional[str] = None


class CandidateResponse(CandidateBase):
    id: int
