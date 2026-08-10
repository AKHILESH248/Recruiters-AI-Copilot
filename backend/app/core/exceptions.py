"""
Custom application exceptions for Recruiter's AI Copilot.
"""

from fastapi import HTTPException, status


class RecruiterAICopilotException(Exception):
    """Base exception for the application."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ResourceNotFoundException(HTTPException):
    """Raised when a requested resource cannot be found."""

    def __init__(self, resource: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} not found.",
        )


class UnauthorizedException(HTTPException):
    """Raised when authentication fails."""

    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized access.",
        )


class ValidationException(HTTPException):
    """Raised when validation fails."""

    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
        )
