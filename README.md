# game-chatbot

This project is a simple command-line game based on Rock–Paper–Scissors, with an extra move called bomb. The program works like a game referee and also plays as the opponent. It checks the user’s input, follows the game rules, keeps score, and shows the result after each round.

Game Rules:-------
The game runs for 3 valid rounds only
Allowed moves are rock, paper, scissors, and bomb
bomb can be used only once in the whole game
bomb beats all other moves
If both players use bomb, the round is a draw
If the user enters an invalid input or tries to use bomb again, the round is wasted and the user must play again

The agent class controls the game flow
Separate functions are used  as tools for validation, prediction, and score updates
Game data like score, rounds, and bomb usage is stored in a single state variable
The bot tries to guess the user’s next move randomly

----Execution steps-------
The whole code is in single file
just run main.py file using command (python main.py)
