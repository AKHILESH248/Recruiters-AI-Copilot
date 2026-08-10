"""
Analysis API routes.
"""

from fastapi import APIRouter, Depends

from app.dependencies.analysis import get_analysis_service
from app.schemas.analysis import AnalysisCreate
from app.services.analysis_service import AnalysisService

router = APIRouter(
    prefix="/analyses",
    tags=["Analyses"],
)


@router.get("/")
def list_analyses(
    service: AnalysisService = Depends(get_analysis_service),
):
    return service.list_analyses()


@router.get("/{analysis_id}")
def get_analysis(
    analysis_id: int,
    service: AnalysisService = Depends(get_analysis_service),
):
    return service.get_analysis(analysis_id)


@router.post("/")
def create_analysis(
    analysis: AnalysisCreate,
    service: AnalysisService = Depends(get_analysis_service),
):
    return service.create_analysis(analysis)
