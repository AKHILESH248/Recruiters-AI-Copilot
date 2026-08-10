"""
Candidate to Job matching service.
"""

from typing import Set


class MatcherService:
    def calculate_match_score(
        self,
        candidate_skills: Set[str],
        required_skills: Set[str],
    ) -> float:
        if not required_skills:
            return 0.0

        matched = candidate_skills.intersection(required_skills)

        return round(
            len(matched) / len(required_skills) * 100,
            2,
        )
