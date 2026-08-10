"""
Candidate API routes.
"""

from fastapi import APIRouter, Depends

from app.dependencies.candidate import get_candidate_service
from app.schemas.candidate import CandidateCreate
from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)


@router.get("/")
def list_candidates(
    service: CandidateService = Depends(get_candidate_service),
):
    return service.list_candidates()


@router.get("/{candidate_id}")
def get_candidate(
    candidate_id: int,
    service: CandidateService = Depends(get_candidate_service),
):
    return service.get_candidate(candidate_id)


@router.post("/")
def create_candidate(
    candidate: CandidateCreate,
    service: CandidateService = Depends(get_candidate_service),
):
    return service.create_candidate(candidate)
