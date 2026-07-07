class RatingManager:
    def downgrade(
        self,
        current_rating: float,
        delta: float,
    ) -> float:
        return max(0, current_rating - delta)

    def increase(
        self,
        current_rating: float,
        delta: float,
    ) -> float:
        return min(5, current_rating + delta)
