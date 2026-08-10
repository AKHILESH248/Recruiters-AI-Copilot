from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="Recruiter's AI Copilot",
    description="AI-powered recruiting platform",
    version="0.1.0",
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Welcome to Recruiter's AI Copilot API",
        "version": "0.1.0",
    }
