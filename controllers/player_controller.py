import json

from models.player import Player
from views.player_view import show_players, ask_player_info, show_player_added


class PlayerController:
    """Handle player-related actions in the application."""

    def __init__(self):
        """Initialize the player controller."""
        pass

    def show_players_ctrl(self):
        """Display the list of players using the player view."""
        show_players()

    def add_player_ctrl(self):
        """Create a new player, save it to JSON, and display a confirmation."""
        # Ask the user for the new player's information through the view.
        player_info = ask_player_info()

        # Build a Player object from the collected data.
        player = Player(
            player_info["first_name"],
            player_info["last_name"],
            player_info["birth_date"],
            player_info["chess_id"],
        )

        # Load the existing players from the JSON file.
        with open("data/players.json", "r", encoding="utf-8") as file:
            players_data = json.load(file)

        # Add the new player to the existing list.
        players_data.append(player.to_dict())

        # Save the updated list back into the JSON file.
        with open("data/players.json", "w", encoding="utf-8") as file:
            json.dump(players_data, file, indent=4, ensure_ascii=False)

        # Display a confirmation message in the view.
        show_player_added(player)
