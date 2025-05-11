import random

def game(user_choice, comp_choice):
    print(f"Computer chose: {comp_choice}")

    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == "rock" and comp_choice == "scissors") or \
         (user_choice == "scissors" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

choices = ["rock", "paper", "scissors"]

# Get valid user input
while True:
    user_choice = input("What is your choice (rock, paper, scissors)? ").lower()
    if user_choice in choices:
        break
    print("That's not a valid option. Try again.")

# Random computer choice
comp_choice = random.choice(choices)

# Play the game
game(user_choice, comp_choice)
