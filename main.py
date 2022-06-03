import random

while True:
    print('"R" for "Rock"', '"P" for "Paper"', '"S" for "Scissors"')
    user_action = input("Enter a choice (R, P, S): ").upper()
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action not in possible_actions:
        print("Please enter a valid input." + " Enter a choice (R, P, S): ")
    else:
        if user_action == "R":
            user_action = "rock"
        elif user_action == "P":
            user_action = "paper"
        elif user_action == "S":
            user_action = "scissors"
        if computer_action == "R":
            computer_action = "rock"
        elif computer_action == "P":
            computer_action = "paper"
        elif computer_action == "S":
            computer_action = "scissors"
        print(f"\nPlayer ({user_action}) : CPU ({computer_action})\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
        elif user_action == "rock":
            if computer_action == "scissors":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "paper":
            if computer_action == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "scissors":
            if computer_action == "paper":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
