from fastapi import FastAPI

app = FastAPI(
    title="Recruiter's AI Copilot",
    description="AI-powered recruiting platform",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {
        "success": True,
        "message": "Welcome to Recruiter's AI Copilot API",
        "version": "0.1.0",
    }


@app.get("/health")
async def health():
    return {
        "success": True,
        "status": "healthy",
    }
