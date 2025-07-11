# Develop a console-based Rock Paper Scissors game in Python
# Game should be modular, allowing for easy updates or rule changes
# Implement game rules:
# - Rock crushes Scissors
# - Scissors cuts Paper
# - Paper covers Rock
# Include user input for selecting options and display game results

import random

def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while user_choice not in choices:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    rules = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice == rules[user_choice]:
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    print("Welcome to Rock Paper Scissors game!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    result = determine_winner(user_choice, computer_choice)

    # Describe the battle with more epic flavor
    battle_descriptions = {
        ('rock', 'scissors'): "With a mighty crash, Rock obliterates Scissors into shards!",
        ('scissors', 'paper'): "Swift as lightning, Scissors slice Paper into ribbons!",
        ('paper', 'rock'): "Paper unfurls and envelops Rock, smothering it in a silent victory!",
        ('scissors', 'rock'): "Rock stands firm and shatters Scissors with unstoppable force!",
        ('paper', 'scissors'): "Scissors dance and shred Paper with razor-sharp precision!",
        ('rock', 'paper'): "Paper glides gracefully, wrapping Rock in an inescapable embrace!"
    }

    if user_choice == computer_choice:
        print("Both chose the same. It's a standoff!")
    else:
        print(battle_descriptions.get((user_choice, computer_choice), 
              battle_descriptions.get((computer_choice, user_choice), "")))

    print(result)

if __name__ == "__main__":
    play_game()

    