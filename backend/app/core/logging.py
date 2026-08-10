"""
Centralized logging configuration for Recruiter's AI Copilot.
"""

import logging
import sys


def configure_logging(level: int = logging.INFO) -> None:
    """
    Configure application-wide logging.
    """

    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
        ],
    )


def get_logger(name: str) -> logging.Logger:
    """
    Return a configured logger.
    """
    return logging.getLogger(name)
