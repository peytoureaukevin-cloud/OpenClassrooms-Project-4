from datetime import datetime

from models.match import Match


class Round:
    def __init__(self, name, matches=None, start_date=None, end_date=None):
        self.name = name
        self.matches = matches if matches is not None else []
        self.start_date = start_date if start_date is not None else self.get_current_datetime()
        self.end_date = end_date

    def __str__(self):
        return f"{self.name} - {len(self.matches)} match(es)"

    def get_current_datetime(self):
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def close_round(self):
        self.end_date = self.get_current_datetime()

    def to_dict(self):
        return {
            "name": self.name,
            "matches": [match.to_dict() for match in self.matches],
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    @classmethod
    def from_dict(cls, data):
        matches = [Match.from_dict(match_data) for match_data in data["matches"]]
        return cls(
            data["name"],
            matches,
            data.get("start_date"),
            data.get("end_date"),
        )
