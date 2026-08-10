"""
Pydantic schemas for Job.
"""

from typing import Optional

from app.schemas.base import BaseSchema


class JobBase(BaseSchema):
    job_title: str
    client_name: Optional[str] = None
    job_location: Optional[str] = None
    employment_type: Optional[str] = None
    experience_required: Optional[str] = None
    salary_range: Optional[str] = None
    job_description: str
    required_skills: Optional[str] = None
    preferred_skills: Optional[str] = None
    recruiter_name: Optional[str] = None
    recruiter_email: Optional[str] = None


class JobCreate(JobBase):
    pass


class JobUpdate(BaseSchema):
    job_title: Optional[str] = None
    client_name: Optional[str] = None
    job_location: Optional[str] = None
    employment_type: Optional[str] = None
    experience_required: Optional[str] = None
    salary_range: Optional[str] = None
    job_description: Optional[str] = None
    required_skills: Optional[str] = None
    preferred_skills: Optional[str] = None
    recruiter_name: Optional[str] = None
    recruiter_email: Optional[str] = None


class JobResponse(JobBase):
    id: int
