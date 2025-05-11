import random

number = random.randint(0, 10)

while True:
    answer = input("Guess the number (0-10): ")

    if not answer.isdigit():
        print("Please enter a valid digit.")
        continue

    answer = int(answer)

    if answer == number:
        print("You got the answer!")
        break