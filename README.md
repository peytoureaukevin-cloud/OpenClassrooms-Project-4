# Chess Tournament Manager

Chess Tournament Manager is a console-based Python application developed in Python.  
It allows the user to manage chess players and tournaments from the terminal.

The project follows the **MVC architecture**:
- **Models**: define the main entities of the project
- **Views**: handle user input and display
- **Controllers**: connect the views and the models

The application uses **JSON files** to store players and tournaments.

---

## Features

- Show all players in alphabetical order
- Add a new player
- Create a tournament
- Automatically create one round with two matches for four players
- Enter match results with score validation
- Save tournaments in a JSON file
- Show the list of tournaments
- Show the details of one tournament
- Show tournament players in alphabetical order
- Show tournament rounds and matches

---

## Project structure

```text
Project-4/
├── main.py
├── README.md
├── requirements.txt
├── data/
│   ├── players.json
│   └── tournaments.json
├── models/
│   ├── __init__.py
│   ├── player.py
│   ├── match.py
│   ├── round.py
│   └── tournament.py
├── views/
│   ├── player_view.py
│   └── tournament_view.py
├── controllers/
│   ├── player_controller.py
│   └── tournament_controller.py
└── flake8_rapport/