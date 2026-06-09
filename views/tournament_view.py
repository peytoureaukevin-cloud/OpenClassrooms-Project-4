from datetime import datetime


class TournamentView:
    def __init__(self):
        pass

    def ask_non_empty_input(self, message):
        while True:
            value = input(message).strip()
            if value:
                return value
            print("This field cannot be empty.")

    def ask_valid_date(self, message):
        while True:
            value = input(message).strip()
            try:
                valid_date = datetime.strptime(value, "%d/%m/%Y")
                return valid_date
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

    def ask_score(self, player_name):
        while True:
            value = input(f"Score for {player_name}: ").strip()
            try:
                score = float(value)
                if score in [0, 0.5, 1]:
                    return score
                print("Score must be 0, 0.5 or 1.")
            except ValueError:
                print("Please enter a valid number.")

    def ask_tournament_info(self):
        tournament_info = {}
        tournament_info["name"] = self.ask_non_empty_input("Tournament name: ")
        tournament_info["location"] = self.ask_non_empty_input("Tournament location: ")
        tournament_info["start_date"] = self.ask_valid_date("Start date (DD/MM/YYYY): ")
        tournament_info["end_date"] = self.ask_valid_date("End date (DD/MM/YYYY): ")
        return tournament_info

    def show_tournament_created(self, tournament):
        print("\nTournament created:")
        print(tournament)

    def show_registered_players(self, players):
        print("\nRegistered players:")
        for player in players:
            print(player)

    def show_round_created(self, round_obj):
        print("\nRound created:")
        print(round_obj)

    def show_match_result(self, match):
        print("\nMatch result:")
        print(match)

    def show_date_order_error(self):
        print("End date cannot be earlier than start date.")

    def show_score_error(self):
        print("Invalid score combination. Allowed results are 1/0, 0/1 or 0.5/0.5.")

    def show_tournaments_list(self, tournaments):
        print("\nTournaments list:")
        for index, tournament in enumerate(tournaments, start=1):
            print(
                f"{index}. {tournament['name']} - "
                f"{tournament['start_date']} to {tournament['end_date']}"
            )

    def ask_tournament_index(self):
        return input("Select tournament number: ")

    def show_tournament_details(self, tournament):
        print("\nTournament details:")
        print(f"Name: {tournament['name']}")
        print(f"Location: {tournament['location']}")
        print(f"Start date: {tournament['start_date']}")
        print(f"End date: {tournament['end_date']}")

    def show_tournament_players(self, tournament):
        print("\nTournament players (alphabetical order):")
        players_sorted = sorted(
            tournament["players"],
            key=lambda player: player["last_name"].lower()
        )

        for player in players_sorted:
            print(
                f"{player['last_name']} {player['first_name']} - "
                f"{player['birth_date']} - {player['chess_id']} - "
                f"Score: {player.get('score', 0)}"
            )

    def show_tournament_rounds_and_matches(self, tournament):
        print("\nTournament rounds and matches:")

        for round_obj in tournament["rounds"]:
            print(f"\n{round_obj['name']}")
            print(f"Start: {round_obj['start_date']}")
            print(f"End: {round_obj['end_date']}")

            for match in round_obj["matches"]:
                player_1 = match[0][0]
                score_1 = match[0][1]
                player_2 = match[1][0]
                score_2 = match[1][1]

                print(
                    f"{player_1['first_name']} {player_1['last_name']} "
                    f"vs "
                    f"{player_2['first_name']} {player_2['last_name']} "
                    f"({score_1} - {score_2})"
                )
