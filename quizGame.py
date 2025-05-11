score = 0
name = input("What is your name? ")
firstAns = input(f"Hello {name}, shall we get started with the quiz (yes/no)? ").lower()

if firstAns == "yes":
    # First question
    answer = input("What is the capital of France? ").lower()
    if answer == "paris":
        print("You got the answer!")
        score += 1
    else:
        print("You didn't get the answer.")

    # Second question
    answer = input("Which animal is known as the 'King of the Jungle'? ").lower()
    if answer == "lion":
        print("You got the answer!")
        score += 1
    else:
        print("You didn't get the answer.")

    # Third question
    answer = input("How many continents are there on Earth? ")
    if answer.isdigit() and int(answer) == 7:
        print("You got the answer!")
        score += 1
    else:
        print("You didn't get the answer.")

    # Fourth question
    answer = input("What is the largest planet in our solar system? ").lower()
    if answer == "jupiter":
        print("You got the answer!")
        score += 1
    else:
        print("You didn't get the answer.")

    # Fifth question
    answer = input("What is the capital of Nigeria? ").lower()
    if answer == "abuja":
        print("You got the answer!")
        score += 1
    else:
        print("You didn't get the answer.")

    percentage = (score / 5) * 100
    print(f"\nYour total score is {score}/5 ({percentage}%).")

elif firstAns == "no":
    print("Alright, maybe next time!")
else:
    print("I don't understand that input.")