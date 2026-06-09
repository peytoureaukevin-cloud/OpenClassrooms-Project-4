import json

from models.player import Player
from views.player_view import show_players, ask_player_info, show_player_added


class PlayerController:
    def __init__(self):
        pass

    def show_players_ctrl(self):
        show_players()

    def add_player_ctrl(self):
        player_info = ask_player_info()

        player = Player(
            player_info["first_name"],
            player_info["last_name"],
            player_info["birth_date"],
            player_info["chess_id"],
        )

        with open("data/players.json", "r", encoding="utf-8") as file:
            players_data = json.load(file)

        players_data.append(player.to_dict())

        with open("data/players.json", "w", encoding="utf-8") as file:
            json.dump(players_data, file, indent=4, ensure_ascii=False)

        show_player_added(player)
