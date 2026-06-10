from datetime import datetime


class TournamentView:
    """Handle user interaction and tournament-related display in the console."""

    def __init__(self):
        """Initialize the tournament view."""
        pass

    def ask_non_empty_input(self, message):
        """Ask for user input until a non-empty value is provided."""
        while True:
            value = input(message).strip()
            if value:
                return value
            print("This field cannot be empty.")

    def ask_valid_date(self, message):
        """Ask for a date and validate the DD/MM/YYYY format."""
        while True:
            value = input(message).strip()
            try:
                valid_date = datetime.strptime(value, "%d/%m/%Y")
                return valid_date
            except ValueError:
                print("Invalid date format. Please use DD/MM/YYYY.")

    def ask_score(self, player_name):
        """Ask for a valid chess score for a given player."""
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
        """Collect the information required to create a tournament."""
        tournament_info = {}
        tournament_info["name"] = self.ask_non_empty_input("Tournament name: ")
        tournament_info["location"] = self.ask_non_empty_input("Tournament location: ")
        tournament_info["start_date"] = self.ask_valid_date("Start date (DD/MM/YYYY): ")
        tournament_info["end_date"] = self.ask_valid_date("End date (DD/MM/YYYY): ")
        return tournament_info

    def show_available_players(self, players):
        """Display all available players with an index for tournament selection."""
        print("\nAvailable players:")
        for index, player in enumerate(players, start=1):
            print(
                f"{index}. {player.first_name} {player.last_name} - "
                f"{player.birth_date} - {player.chess_id}"
            )

    def ask_player_selection(self, max_index):
        """Ask the user to select players by entering comma-separated numbers."""
        while True:
            choice = input(
                "Select player numbers separated by commas "
                "(example: 1,2,3,4): "
            ).strip()

            if not choice:
                print("Selection cannot be empty.")
                continue

            parts = [part.strip() for part in choice.split(",")]

            if not all(part.isdigit() for part in parts):
                print("Please enter only numbers separated by commas.")
                continue

            indexes = [int(part) for part in parts]

            if len(indexes) != len(set(indexes)):
                print("You cannot select the same player twice.")
                continue

            if any(index < 1 or index > max_index for index in indexes):
                print("One or more selected numbers are invalid.")
                continue

            return indexes

    def show_invalid_player_count_error(self):
        """Display an error when the selected number of players is invalid."""
        print("A tournament requires an even number of selected players.")

    def show_tournament_created(self, tournament):
        """Display a confirmation once a tournament has been created."""
        print("\nTournament created:")
        print(tournament)

    def show_registered_players(self, players):
        """Display the players registered in the tournament."""
        print("\nRegistered players:")
        for player in players:
            print(player)

    def show_round_created(self, round_obj):
        """Display information about a created round."""
        print("\nRound created:")
        print(round_obj)

    def show_match_result(self, match):
        """Display the result of a match."""
        print("\nMatch result:")
        print(match)

    def show_date_order_error(self):
        """Display an error when the end date is earlier than the start date."""
        print("End date cannot be earlier than start date.")

    def show_score_error(self):
        """Display an error for an invalid score combination."""
        print("Invalid score combination. Allowed results are 1/0, 0/1 or 0.5/0.5.")

    def show_tournaments_list(self, tournaments):
        """Display the list of saved tournaments."""
        print("\nTournaments list:")
        for index, tournament in enumerate(tournaments, start=1):
            print(
                f"{index}. {tournament['name']} - "
                f"{tournament['start_date']} to {tournament['end_date']}"
            )

    def ask_tournament_index(self):
        """Ask the user to select a tournament by its number."""
        return input("Select tournament number: ")

    def show_tournament_details(self, tournament):
        """Display the main information of one tournament."""
        print("\nTournament details:")
        print(f"Name: {tournament['name']}")
        print(f"Location: {tournament['location']}")
        print(f"Start date: {tournament['start_date']}")
        print(f"End date: {tournament['end_date']}")

    def show_tournament_players(self, tournament):
        """Display tournament players in alphabetical order."""
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
        """Display all rounds of a tournament and the matches they contain."""
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
