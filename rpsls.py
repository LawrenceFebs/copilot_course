# TODO: Develop a console-based Rock Paper Scissors Lizard Spock game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Scissors decapitate lizard
# - Scissors cuts paper
# - Paper covers rock 
# - Rock crushes lizard 
# - Lizard poisons Spock 
# - Spock smashes scissors 
# - Lizard eats paper 
# - Paper disproves Spock 
# - Spock vaporizes rock 
# - Rock crushes scissors
# Include user input for selecting options and display game results

import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors, lizard, spock): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice in rules[user_choice]:
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    print("Welcome to Rock Paper Scissors Lizard Spock game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()

# This code implements a console-based Rock Paper Scissors Lizard Spock game.
# It allows the user to input their choice, randomly selects a choice for the computer,
# and determines the winner based on the defined rules. The game can be easily extended or modified
# to include additional features or rules.
# The game is modular, allowing for easy updates or rule changes.
# The rules are clearly defined in a dictionary, making it easy to add or change rules in the future.
# The game includes user input validation to ensure valid choices are made.
# The game is structured to be easily readable and maintainable.
# The game can be run in a console environment, making it accessible for users without a graphical interface.
# The game can be easily extended to include more features, such as score tracking or multiple rounds
# The game can be easily modified to include additional choices or rules, such as adding new characters or actions.
# The game can be easily tested and debugged due to its modular structure.
# The game can be easily integrated into larger projects or applications.
# The game can be easily adapted for different platforms or environments, such as web or mobile applications