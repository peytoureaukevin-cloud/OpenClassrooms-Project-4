from models.player import Player


class Match:
    """Represent a match between two players and store the result."""

    def __init__(self, player_1, player_2, score_1=0, score_2=0):
        """Initialize a match with two players and optional starting scores."""
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __str__(self):
        """Return a readable string representation of the match."""
        return (
            f"{self.player_1.first_name} {self.player_1.last_name} "
            f"vs "
            f"{self.player_2.first_name} {self.player_2.last_name} "
            f"({self.score_1} - {self.score_2})"
        )

    def player_snapshot(self, player):
        """Return a lightweight snapshot of a player for match serialization."""
        return {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birth_date": player.birth_date,
            "chess_id": player.chess_id,
        }

    def to_dict(self):
        """Convert the match into a JSON-serializable structure."""
        # Each match is stored as two entries: one player snapshot and one score.
        return [
            [self.player_snapshot(self.player_1), self.score_1],
            [self.player_snapshot(self.player_2), self.score_2],
        ]

    @classmethod
    def from_dict(cls, data):
        """Rebuild a Match object from saved JSON data."""
        # Support the current list-based format used in the project.
        if isinstance(data, list):
            player_1 = Player.from_dict(data[0][0])
            score_1 = data[0][1]
            player_2 = Player.from_dict(data[1][0])
            score_2 = data[1][1]
            return cls(player_1, player_2, score_1, score_2)

        # Support the older dictionary-based format for compatibility.
        if isinstance(data, dict):
            player_1 = Player.from_dict(data["player_1"])
            score_1 = data["score_1"]
            player_2 = Player.from_dict(data["player_2"])
            score_2 = data["score_2"]
            return cls(player_1, player_2, score_1, score_2)

        raise ValueError("Unsupported match data format.")
