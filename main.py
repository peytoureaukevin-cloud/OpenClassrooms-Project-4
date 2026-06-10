from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


def main():
    """Run the main menu loop of the chess tournament application."""
    player_ctrl = PlayerController()
    tournament_ctrl = TournamentController()
    running = True

    while running:
        # Display the main menu options available to the user.
        print("\nChess Tournament Manager")
        print("1. Show players")
        print("2. Add player")
        print("3. Create tournament")
        print("4. Show tournaments")
        print("5. Show one tournament")
        print("6. Resume tournament")
        print("7. Exit")

        choice = input("Your choice: ")

        # Redirect the user choice to the appropriate controller action.
        if choice == "1":
            player_ctrl.show_players_ctrl()
        elif choice == "2":
            player_ctrl.add_player_ctrl()
        elif choice == "3":
            tournament_ctrl.create_tournament_ctrl()
        elif choice == "4":
            tournament_ctrl.show_tournaments_ctrl()
        elif choice == "5":
            tournament_ctrl.show_one_tournament_ctrl()
        elif choice == "6":
            tournament_ctrl.resume_tournament_ctrl()
        elif choice == "7":
            print("Goodbye")
            running = False
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
