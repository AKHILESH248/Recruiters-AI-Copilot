"""
OpenAI integration service.
"""

from typing import Optional

from app.core.config import settings


class OpenAIService:
    """
    Wrapper around the OpenAI API.

    Package 1 provides a placeholder implementation.
    Future packages will integrate the OpenAI Responses API.
    """

    def __init__(self):
        self.api_key = settings.OPENAI_API_KEY

    def is_configured(self) -> bool:
        return bool(self.api_key)

    def summarize_text(self, text: str) -> str:
        """
        Placeholder summary.
        """
        return text[:500] if text else ""

    def extract_skills(self, text: str) -> list[str]:
        """
        Placeholder skill extraction.
        """
        return []

    def analyze_resume(
        self,
        resume_text: str,
        job_description: Optional[str] = None,
    ) -> dict:
        """
        Placeholder resume analysis.
        """
        return {
            "summary": self.summarize_text(resume_text),
            "skills": self.extract_skills(resume_text),
            "match_score": None,
            "job_description": job_description,
        }
