"""
Candidate ranking service.
"""

from typing import List, Dict


class RankingService:
    """
    Rank candidates based on AI match scores.
    """

    def rank_candidates(
        self,
        candidates: List[Dict],
    ) -> List[Dict]:
        """
        Sort candidates by match score (highest first).
        """

        return sorted(
            candidates,
            key=lambda candidate: candidate.get("match_score", 0),
            reverse=True,
        )

    def top_candidates(
        self,
        candidates: List[Dict],
        limit: int = 10,
    ) -> List[Dict]:
        """
        Return the highest-ranked candidates.
        """

        return self.rank_candidates(candidates)[:limit]
