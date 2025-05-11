def gameplay():
    print("\nYou wake up at the edge of a mysterious forest. You don’t remember how you got here, but you feel an urge to move forward.")
    first = input("Will you (a) Enter the forest or (b) Follow a small path around it? (a/b): ").lower()

    if first == "a":
        print("\nYou hear eerie whispers and notice glowing eyes in the distance.")
        second = input("What do you do? (a) Climb a nearby tree to get a better view or (b) Approach the glowing eyes? (a/b): ").lower()

        if second == "a":
            print("\nYou fall from the tree, break your spine, and are mysteriously stabbed 15 times. You died.")
        elif second == "b":
            print("\nAs you approach the eyes, you notice a man in glasses stuck in a thorny vine.")
            third = input("What do you do? (a) Help the man or (b) Leave him and keep walking? (a/b): ").lower()

            if third == "a":
                print("\nYou help the man. He thanks you and insists on joining your journey.")
                fourth = input("Will you (a) Let him follow or (b) Politely decline? (a/b): ").lower()

                if fourth == "a":
                    print("\nYou and the man walk together, but suddenly you black out. You are never seen again.")
                elif fourth == "b":
                    print("\nHe thanks you for your kindness and leaves. You move forward safely.")
                    print("🎉 You have passed the first stage. CONGRATULATIONS!")
                else:
                    print("Invalid choice.")
            elif third == "b":
                print("\nThe man frees himself, enraged by your coldness. He lunges at you and ends your journey violently.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

    elif first == "b":
        print("\nYou take the path... but fall into a hidden pit and slowly starve. You died.")
    else:
        print("Invalid choice.")


# Game start
name = input("What is your name? ")
ans = input(f"\nHello {name}, welcome to 'The Forest of Whispers'. Are you ready to begin? (yes/no): ").lower()

if ans == "yes":
    gameplay()
elif ans == "no":
    print("Maybe next time. Goodbye!")
else:
    print("That wasn't a valid option. Please restart the game.")
