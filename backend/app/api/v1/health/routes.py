from fastapi import APIRouter

router = APIRouter(prefix="/health")


@router.get("/")
async def health_check():
    return {
        "success": True,
        "status": "healthy",
        "service": "Recruiter's AI Copilot API",
        "version": "0.1.0",
    }
