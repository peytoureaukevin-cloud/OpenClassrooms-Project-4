class Player:
    def __init__(self, first_name: str, last_name, birth_date, chess_id, score=0):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.chess_id = chess_id
        self.score = score

    def __str__(self):
        return (
            f"{self.first_name} {self.last_name} - "
            f"{self.birth_date} - {self.chess_id} - Score: {self.score}"
        )

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
            "chess_id": self.chess_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["first_name"],
            data["last_name"],
            data["birth_date"],
            data["chess_id"],
            data.get("score", 0),
        )
