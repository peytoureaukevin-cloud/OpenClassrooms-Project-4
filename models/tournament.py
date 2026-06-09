from models.player import Player
from models.round import Round


class Tournament:
    def __init__(
        self,
        name: str,
        location,
        start_date,
        end_date,
        rounds_number=4,
        current_round=1,
        rounds=None,
        players=None,
        description=""
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds_number = rounds_number
        self.current_round = current_round
        self.rounds = rounds if rounds is not None else []
        self.players = players if players is not None else []
        self.description = description

    def __str__(self):
        return (
            f"{self.name} - {self.location} - "
            f"{self.start_date} to {self.end_date}"
        )

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds_number": self.rounds_number,
            "current_round": self.current_round,
            "rounds": [round_obj.to_dict() for round_obj in self.rounds],
            "players": [player.to_dict() for player in self.players],
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data):
        players = [Player.from_dict(player_data) for player_data in data["players"]]
        rounds = [Round.from_dict(round_data) for round_data in data["rounds"]]

        return cls(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data.get("rounds_number", 4),
            data.get("current_round", 1),
            rounds,
            players,
            data.get("description", ""),
        )
