import json
import random

from models.player import Player
from models.match import Match
from models.round import Round
from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:
    """Handle tournament creation, round generation, persistence, and reporting."""

    def __init__(self):
        """Initialize the tournament controller with its associated view."""
        self.view = TournamentView()

    def ask_and_apply_match_scores(self, match):
        """Ask the user for a valid match result and update both match and player scores."""
        while True:
            score_1 = self.view.ask_score(
                f"{match.player_1.first_name} {match.player_1.last_name}"
            )
            score_2 = self.view.ask_score(
                f"{match.player_2.first_name} {match.player_2.last_name}"
            )

            if (
                (score_1 == 1 and score_2 == 0)
                or (score_1 == 0 and score_2 == 1)
                or (score_1 == 0.5 and score_2 == 0.5)
            ):
                break

            self.view.show_score_error()

        match.score_1 = score_1
        match.score_2 = score_2
        match.player_1.score += score_1
        match.player_2.score += score_2

    def get_previous_pairs(self, rounds):
        """Return a set of player pairs that have already played against each other."""
        previous_pairs = set()

        for round_obj in rounds:
            for match in round_obj.matches:
                pair = frozenset(
                    {
                        match.player_1.chess_id,
                        match.player_2.chess_id,
                    }
                )
                previous_pairs.add(pair)

        return previous_pairs

    def generate_first_round_matches(self, players):
        """Generate the first round by shuffling players randomly and pairing them."""
        players_for_round = players[:]
        random.shuffle(players_for_round)

        matches = []
        for index in range(0, len(players_for_round), 2):
            matches.append(Match(players_for_round[index], players_for_round[index + 1]))

        return matches

    def build_matches_without_rematch(self, available_players, previous_pairs):
        """Build valid matches recursively while avoiding rematches."""
        if not available_players:
            return []

        player_1 = available_players[0]

        for index in range(1, len(available_players)):
            player_2 = available_players[index]
            pair = frozenset({player_1.chess_id, player_2.chess_id})

            if pair in previous_pairs:
                continue

            remaining_players = available_players[1:index] + available_players[index + 1:]
            remaining_matches = self.build_matches_without_rematch(
                remaining_players,
                previous_pairs,
            )

            if remaining_matches is not None:
                return [Match(player_1, player_2)] + remaining_matches

        return None

    def generate_next_round_matches(self, players, previous_pairs):
        """Generate the next round based on scores while avoiding previous pairings."""
        players_for_round = players[:]
        random.shuffle(players_for_round)

        sorted_players = sorted(
            players_for_round,
            key=lambda player: (-player.score, player.last_name.lower(), player.first_name.lower()),
        )

        return self.build_matches_without_rematch(sorted_players, previous_pairs)

    def load_players_for_tournament(self):
        """Load all saved players and reset their score for a new tournament."""
        with open("data/players.json", "r", encoding="utf-8") as file:
            players_data = json.load(file)

        players = []
        for player_data in players_data:
            players.append(
                Player(
                    player_data["first_name"],
                    player_data["last_name"],
                    player_data["birth_date"],
                    player_data["chess_id"],
                    0,
                )
            )

        return players

    def select_players_for_tournament(self, available_players):
        """Let the user choose which players will participate in the tournament."""
        while True:
            self.view.show_available_players(available_players)
            selected_indexes = self.view.ask_player_selection(len(available_players))

            if len(selected_indexes) < 2 or len(selected_indexes) % 2 != 0:
                self.view.show_invalid_player_count_error()
                continue

            selected_players = []
            for index in selected_indexes:
                selected_players.append(available_players[index - 1])

            return selected_players

    def load_tournaments(self):
        """Load saved tournaments from JSON and rebuild Tournament objects."""
        with open("data/tournaments.json", "r", encoding="utf-8") as file:
            tournaments_data = json.load(file)

        return [Tournament.from_dict(data) for data in tournaments_data]

    def save_tournament(self, tournament):
        """Append a tournament to the JSON storage file."""
        with open("data/tournaments.json", "r", encoding="utf-8") as file:
            tournaments_data = json.load(file)

        tournaments_data.append(tournament.to_dict())

        with open("data/tournaments.json", "w", encoding="utf-8") as file:
            json.dump(tournaments_data, file, indent=4, ensure_ascii=False)

    def play_round(self, round_obj):
        """Play all matches of a round, then close the round."""
        for match in round_obj.matches:
            self.ask_and_apply_match_scores(match)

        round_obj.close_round()

    def create_tournament_ctrl(self):
        """Create a tournament, generate and play its rounds, then save and display it."""
        while True:
            tournament_info = self.view.ask_tournament_info()

            start_date = tournament_info["start_date"]
            end_date = tournament_info["end_date"]

            if end_date >= start_date:
                break

            self.view.show_date_order_error()

        tournament = Tournament(
            tournament_info["name"],
            tournament_info["location"],
            start_date.strftime("%d/%m/%Y"),
            end_date.strftime("%d/%m/%Y"),
        )

        available_players = self.load_players_for_tournament()
        tournament.players = self.select_players_for_tournament(available_players)

        max_rounds_without_rematch = len(tournament.players) - 1
        if tournament.rounds_number > max_rounds_without_rematch:
            tournament.rounds_number = max_rounds_without_rematch

        for round_number in range(1, tournament.rounds_number + 1):
            if round_number == 1:
                matches = self.generate_first_round_matches(tournament.players)
            else:
                previous_pairs = self.get_previous_pairs(tournament.rounds)
                matches = self.generate_next_round_matches(
                    tournament.players,
                    previous_pairs,
                )

                if matches is None:
                    print("\nNo valid pairings available without rematch.")
                    break

            round_obj = Round(f"Round {round_number}", matches)
            self.play_round(round_obj)
            tournament.rounds.append(round_obj)
            tournament.current_round = round_number

        self.save_tournament(tournament)

        self.view.show_tournament_created(tournament)
        self.view.show_registered_players(tournament.players)

        for round_obj in tournament.rounds:
            self.view.show_round_created(round_obj)
            for match in round_obj.matches:
                self.view.show_match_result(match)

    def show_tournaments_ctrl(self):
        """Display the list of all saved tournaments."""
        tournaments = self.load_tournaments()

        if not tournaments:
            print("\nNo tournaments found.")
            return

        tournaments_data = [tournament.to_dict() for tournament in tournaments]
        self.view.show_tournaments_list(tournaments_data)

    def show_one_tournament_ctrl(self):
        """Display the full details of one selected tournament."""
        tournaments = self.load_tournaments()

        if not tournaments:
            print("\nNo tournaments found.")
            return

        tournaments_data = [tournament.to_dict() for tournament in tournaments]
        self.view.show_tournaments_list(tournaments_data)

        while True:
            choice = self.view.ask_tournament_index().strip()

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(tournaments):
                    tournament = tournaments[index].to_dict()
                    self.view.show_tournament_details(tournament)
                    self.view.show_tournament_players(tournament)
                    self.view.show_tournament_rounds_and_matches(tournament)
                    break

            print("Invalid tournament number.")

    def resume_tournament_ctrl(self):
        """Load one saved tournament as an object and display a confirmation."""
        tournaments = self.load_tournaments()

        if not tournaments:
            print("\nNo tournaments found.")
            return

        tournaments_data = [tournament.to_dict() for tournament in tournaments]
        self.view.show_tournaments_list(tournaments_data)

        while True:
            choice = self.view.ask_tournament_index().strip()

            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(tournaments):
                    tournament = tournaments[index]
                    print("\nTournament loaded as object:")
                    print(tournament)
                    break

            print("Invalid tournament number.")
