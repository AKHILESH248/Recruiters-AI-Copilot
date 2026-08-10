"""
Common schemas shared across the application.
"""

from app.schemas.base import BaseSchema


class MessageResponse(BaseSchema):
    message: str


class HealthResponse(BaseSchema):
    status: str
    version: str


class Pagination(BaseSchema):
    page: int
    size: int
    total: int
