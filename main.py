

import random

# ------------------Game State Dictionary----------------


game_state = {
    "valid_round": 1,
    "user_score": 0,
    "bot_score": 0,
    "user_bomb_used": False,
    "bot_bomb_used": False,
    "user_moves": []
}

# ------------------Agent Class--------------------------

class Agent:
    def validate_move(self, move):
        move = move.lower().strip()
        valid_moves = ["rock", "paper", "scissors", "bomb"]

        if move not in valid_moves:
            return False, "Invalid input"

        if move == "bomb" and game_state["user_bomb_used"]:
            return False, "You have already used bomb"

        return True, move

    def predict_bot_move(self):
        if not game_state["user_moves"]:
            return random.choice(["rock", "paper", "scissors"])

        most_used = max(
            set(game_state["user_moves"]),
            key=game_state["user_moves"].count
        )

        counter = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }

        bot_move = counter.get(most_used, random.choice(["rock", "paper", "scissors"]))

        # little randomness
        if random.random() < 0.3:
            bot_move = random.choice(["rock", "paper", "scissors"])

        # bomb only once
        if not game_state["bot_bomb_used"] and random.random() < 0.1:
            bot_move = "bomb"

        return bot_move

    def decide_winner(self, user_move, bot_move):
        if user_move == bot_move:
            return "draw"

        if user_move == "bomb":
            return "user"

        if bot_move == "bomb":
            return "bot"

        rules = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }

        return "user" if rules[user_move] == bot_move else "bot"

    def update_state(self, user_move, bot_move, winner):
        if user_move == "bomb":
            game_state["user_bomb_used"] = True

        if bot_move == "bomb":
            game_state["bot_bomb_used"] = True

        if winner == "user":
            game_state["user_score"] += 1
        elif winner == "bot":
            game_state["bot_score"] += 1

        game_state["user_moves"].append(user_move)
        game_state["valid_round"] += 1


# ----------------Game Starts function-----------------------------


def start_game():
    agent = Agent()

    print("""
Rock–Paper–Scissors–Plus
Exactly 3 valid rounds

Rules:
- Moves: rock, paper, scissors, bomb
- Bomb can be used only once
- Invalid input or second bomb → round wasted
""")

    while game_state["valid_round"] <= 3:
        print(f"Valid Round {game_state['valid_round']}")
        user_input = input("Enter your move: ")

        valid, result = agent.validate_move(user_input)

        if not valid:
            print(result)
            print("Round wasted, please play again\n")
            continue   # round NOT counted

        user_move = result
        bot_move = agent.predict_bot_move()
        winner = agent.decide_winner(user_move, bot_move)

        agent.update_state(user_move, bot_move, winner)

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")

        if winner == "draw":
            print("Result: Draw\n")
        else:
            print(f"Result: {winner.capitalize()} wins\n")

    print("****** Game Over *******")
    print(f"Final Score → You: {game_state['user_score']} | Bot: {game_state['bot_score']}")

    if game_state["user_score"] > game_state["bot_score"]:
        print("You win!")
    elif game_state["bot_score"] > game_state["user_score"]:
        print("Bot wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    start_game()
