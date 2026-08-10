from fastapi import APIRouter

from app.api.v1.analysis.routes import router as analysis_router
from app.api.v1.candidate.routes import router as candidate_router
from app.api.v1.health.routes import router as health_router
from app.api.v1.job.routes import router as job_router
from app.api.v1.resume.routes import router as resume_router

api_v1_router = APIRouter(prefix="/api/v1")

api_v1_router.include_router(
    health_router,
    tags=["Health"],
)

api_v1_router.include_router(
    candidate_router,
)

api_v1_router.include_router(
    job_router,
)

api_v1_router.include_router(
    resume_router,
)

api_v1_router.include_router(
    analysis_router,
)
