import random

while True:
    computer = random.randint(1, 100)
    attempts = 0
    chances_left = 10

    print("\nNew Game Started! Guess the number between 1 and 100.")

    while True:
        try:
            user = int(input("Enter a number: "))
            attempts += 1

            if user > computer:
                chances_left -= 1
                print("Too high.")
                print(f"Chances left: {chances_left}")

            elif user < computer:
                chances_left -= 1
                print("Too low.")
                print(f"Chances left: {chances_left}")

            else:
                print("Correct! You guessed the number.")
                print(f"You took {attempts} attempts.")
                break

            if chances_left == 0:
                print(f"No chances left. The correct number was {computer}.")
                break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing.")
        break
