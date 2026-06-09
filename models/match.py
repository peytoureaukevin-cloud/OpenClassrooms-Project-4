from models.player import Player


class Match:
    def __init__(self, player_1, player_2, score_1=0, score_2=0):
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_1 = score_1
        self.score_2 = score_2

    def __str__(self):
        return (
            f"{self.player_1.first_name} {self.player_1.last_name} "
            f"vs "
            f"{self.player_2.first_name} {self.player_2.last_name} "
            f"({self.score_1} - {self.score_2})"
        )

    def player_snapshot(self, player):
        return {
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birth_date": player.birth_date,
            "chess_id": player.chess_id,
        }

    def to_dict(self):
        return [
            [self.player_snapshot(self.player_1), self.score_1],
            [self.player_snapshot(self.player_2), self.score_2],
        ]

    @classmethod
    def from_dict(cls, data):
        if isinstance(data, list):
            player_1 = Player.from_dict(data[0][0])
            score_1 = data[0][1]
            player_2 = Player.from_dict(data[1][0])
            score_2 = data[1][1]
            return cls(player_1, player_2, score_1, score_2)

        if isinstance(data, dict):
            player_1 = Player.from_dict(data["player_1"])
            score_1 = data["score_1"]
            player_2 = Player.from_dict(data["player_2"])
            score_2 = data["score_2"]
            return cls(player_1, player_2, score_1, score_2)

        raise ValueError("Unsupported match data format.")
