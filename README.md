# Chess Tournament Manager

Chess Tournament Manager is a console-based Python application developed as part of an OpenClassrooms project. The purpose of the application is to help a chess club manage its players and tournaments directly from the terminal. The program allows the user to register players, create tournaments, select which players participate in a tournament, generate rounds and matches, enter match results, update player scores, save tournament data, reload saved tournaments, and display tournament reports. The project follows the MVC architecture: the models define the business objects, the views manage user input and console display, and the controllers manage the application logic. Persistent data is stored in JSON files.

Before using the project, make sure that Python 3 is installed on your machine. You can check your Python version by opening a terminal and running the following command:

python3 --version

Once Python is available, open a terminal in the root folder of the project and install the dependencies with this command:

python3 -m pip install -r requirements.txt

After the dependencies are installed, you can launch the program directly from the root folder of the project with the following command:

python3 main.py

This command starts the application in the terminal. When the program launches correctly, the following menu is displayed:

Chess Tournament Manager
1. Show players
2. Add player
3. Create tournament
4. Show tournaments
5. Show one tournament
6. Resume tournament
7. Exit

The first option, Show players, displays all registered players stored in data/players.json. Players are shown in alphabetical order so the list is easier to read.

The second option, Add player, allows the user to register a new player. The program asks for the player's first name, last name, birth date, and chess ID. Several validation rules are applied: fields cannot be empty, the birth date must follow the format DD/MM/YYYY, and the chess ID must follow the format 2 letters followed by 5 digits. For example, GK63043 is a valid chess ID. Once the input is validated, the player is saved in data/players.json.

The third option, Create tournament, creates a new tournament. The program asks for the tournament name, the location, the start date, and the end date. Dates must follow the format DD/MM/YYYY, and the end date cannot be earlier than the start date. After the tournament information is entered, the program loads the available players and displays them in the terminal so the user can choose which players will take part in the tournament. The player selection is done by entering numbers separated by commas.

Example of player selection:

Available players:
1. Garry Kasparov - 13/04/1963 - GK63043
2. Deep Blue - 01/01/1990 - DB01010
3. Magnus Carlsen - 30/11/1990 - MC30119
4. Hikaru Nakamura - 09/12/1987 - HN09128

Select player numbers separated by commas (example: 1,2,3,4):

The selection must respect several rules: it cannot be empty, all selected numbers must exist, the same player cannot be selected twice, at least two players must be selected, and the number of selected players must be even. Once the players are selected, the tournament begins. The first round is generated randomly. The following rounds are generated according to player scores, and rematches are avoided when possible. For each match, the user enters the result directly in the terminal. Only valid chess results are accepted: 1 and 0, 0 and 1, or 0.5 and 0.5. After each match, the cumulative player scores are updated automatically. When the tournament is complete, it is saved in data/tournaments.json.

The fourth option, Show tournaments, displays the list of all saved tournaments.

The fifth option, Show one tournament, displays the details of one selected tournament, including its general information, the registered players, the rounds, the matches, and the results.

The sixth option, Resume tournament, loads a saved tournament from data/tournaments.json and rebuilds it as a Python object.

The seventh option, Exit, closes the program.

The project stores its data in two JSON files. The file data/players.json stores all registered players. The file data/tournaments.json stores all created tournaments, including tournament information, selected players, rounds, matches, match results, and cumulative scores. This allows the application to persist data between executions.

The project is organized with the following structure:

Project-4/
├── main.py
├── README.md
├── requirements.txt
├── .flake8
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
    └── index.html

The models folder contains the business entities of the application: Player, Match, Round, and Tournament. The views folder handles all terminal interaction, including user input, error messages, and display. The controllers folder contains the application logic, including player creation, tournament creation, player selection, round generation, score application, JSON loading and saving, and the interaction between models and views.

Code quality is checked with flake8. To run flake8 in the terminal from the root folder of the project, use the following command:

python3 -m flake8 .

To generate the HTML flake8 report, run:

python3 -m flake8 --format=html --htmldir=flake8_rapport

The HTML report is then available in:

flake8_rapport/index.html

This project is a terminal-based application that uses object-oriented programming, JSON persistence, and the MVC design pattern to provide a structured chess tournament manager.