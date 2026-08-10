"""
Security helpers for Recruiter's AI Copilot.

This module is intentionally lightweight for Package 1.
Future packages will extend it with:
- JWT authentication
- Password hashing
- OAuth2
- API key validation
"""

from secrets import token_urlsafe


def generate_secret_key(length: int = 32) -> str:
    """
    Generate a cryptographically secure random secret.
    """
    return token_urlsafe(length)


def mask_api_key(api_key: str) -> str:
    """
    Mask an API key before logging or displaying it.
    """
    if not api_key:
        return ""

    if len(api_key) <= 8:
        return "*" * len(api_key)

    return f"{api_key[:4]}{'*' * (len(api_key) - 8)}{api_key[-4:]}"
