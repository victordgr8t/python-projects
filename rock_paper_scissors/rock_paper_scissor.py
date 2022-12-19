import random

# This function takes in the player's choice (either "rock", "paper", or "scissors")
# and returns the computer's choice, randomly selected from the same three options.


def get_computer_choice(player_choice):
    choices = ["rock", "paper", "scissors"]

    # Return a random choice from the options.
    return random.choice(choices)

# This function takes in the player's choice and the computer's choice,
# and returns a string representing the outcome of the game.
# The possible return values are "player wins", "computer wins", and "tie".


def get_game_result(player_choice, computer_choice):
    if player_choice == "rock" and computer_choice == "scissors":
        return "player wins"
    elif player_choice == "rock" and computer_choice == "paper":
        return "computer wins"
    elif player_choice == "paper" and computer_choice == "rock":
        return "player wins"
    elif player_choice == "paper" and computer_choice == "scissors":
        return "computer wins"
    elif player_choice == "scissors" and computer_choice == "rock":
        return "computer wins"
    elif player_choice == "scissors" and computer_choice == "paper":
        return "player wins"
    else:
        return "tie"


# This is the main game loop. It continues to run until the player
# decides to quit.
while True:
    player_choice = input(
        "Please enter your choice (rock, paper, scissors, or quit): ")
    if player_choice.lower() == "quit":
        break

    computer_choice = get_computer_choice(player_choice)
    result = get_game_result(player_choice, computer_choice)
    print(f"You chose {player_choice}, the computer chose {computer_choice}.")
    print(f"Result: {result}.")
