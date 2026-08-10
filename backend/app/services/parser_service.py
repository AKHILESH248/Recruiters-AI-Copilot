"""
Resume and Job Description parsing service.
"""

from pathlib import Path


class ParserService:
    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".docx",
        ".txt",
    }

    def is_supported(self, filename: str) -> bool:
        return Path(filename).suffix.lower() in self.SUPPORTED_EXTENSIONS

    def parse_text(self, text: str) -> str:
        """
        Placeholder parser.
        Future packages will implement PDF/DOCX extraction.
        """
        return text.strip()
