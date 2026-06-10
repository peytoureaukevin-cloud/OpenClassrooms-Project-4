class Player:
    """Represent a chess player and store identifying information and score."""

    def __init__(self, first_name: str, last_name, birth_date, chess_id, score=0):
        """Initialize a player with identity data and an optional score."""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def __str__(self):
        """Return a readable string representation of the player."""
        return (
            f"{self.first_name} {self.last_name} - "
            f"{self.birth_date} - {self.chess_id} - Score: {self.score}"
        )

    def to_dict(self):
        """Convert the player into a JSON-serializable dictionary."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Player object from saved JSON data."""
        return cls(
            data["first_name"],
            data["last_name"],
            data["birth_date"],
            data["chess_id"],
            data.get("score", 0),
        )
