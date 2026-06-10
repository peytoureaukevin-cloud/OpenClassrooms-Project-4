import json
import re


def show_players():
    """Load and display all registered players in alphabetical order."""
    with open("data/players.json", "r", encoding="utf-8") as file:
        players = json.load(file)

    # Sort players by last name for a clearer report.
    players_sorted = sorted(players, key=lambda player: player["last_name"].lower())

    print("\nPlayers list:")
    for player in players_sorted:
        print(
            f"{player['first_name']} {player['last_name']} - "
            f"Birth date: {player['birth_date']} - "
            f"Chess ID: {player['chess_id']}"
        )


def ask_non_empty_input(message):
    """Ask for user input until a non-empty value is provided."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("This field cannot be empty.")


def ask_birth_date():
    """Ask for a birth date and validate the DD/MM/YYYY format."""
    while True:
        value = input("Birth date (DD/MM/YYYY): ").strip()
        if re.fullmatch(r"\d{2}/\d{2}/\d{4}", value):
            return value
        print("Invalid date format. Please use DD/MM/YYYY.")


def ask_chess_id():
    """Ask for a chess ID and validate the expected format."""
    while True:
        value = input("Chess ID (2 letters + 5 digits): ").strip().upper()
        if re.fullmatch(r"[A-Z]{2}\d{5}", value):
            return value
        print("Invalid chess ID format. Please use 2 letters followed by 5 digits.")


def ask_player_info():
    """Collect all required information to create a new player."""
    player_info = {}
    player_info["first_name"] = ask_non_empty_input("First name: ")
    player_info["last_name"] = ask_non_empty_input("Last name: ")
    player_info["birth_date"] = ask_birth_date()
    player_info["chess_id"] = ask_chess_id()
    return player_info


def show_player_added(player):
    """Display a confirmation message after a player has been added."""
    print("\nPlayer added:")
    print(player)
