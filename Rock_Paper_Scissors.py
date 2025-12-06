import random

while True:
    options = ["rock", "paper", "scissors"]
    computer = random.choice(options)

    print("\nNew Game Started! Choose rock, paper, or scissors.\n")

    while True:
        user = input("Enter your choice (rock, paper, scissors): ").lower()

        if user not in options:
            print("Invalid input. Please choose only from rock, paper or scissors.")
            continue

        if (user == "rock" and computer == "scissors") or \
           (user == "scissors" and computer == "paper") or \
           (user == "paper" and computer == "rock"):
            print(f"You win! Computer chose {computer}, you chose {user}.")
            break

        elif user == computer:
            print(f"It's a tie. Both chose {user}.")

        else:
            print(f"You lose. Computer chose {computer}, you chose {user}.")
            break

    replay_game = input("\nDo you want to play again? (yes/no): ").lower()
    if replay_game not in ["yes", "y"]:
        print("Thanks for playing.")
        break
