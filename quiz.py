print("Welcome to my Quiz Mania")

while True:   # allows user to replay
    suggestion = input("Do you want to play the quiz? (yes/no): ").lower()

    if suggestion != "yes":
        print("Thank you for visiting.")
        break

    print("\nI will ask 5 questions. You need to score at least 4 out of 5.\n")

    count = 0
    wrong = 0

    # Question bank for cleaner code
    questions = [
        ["Which animal is known as the 'Ship of the Desert'?", "camel"],
        ["How many days are there in a week?", ["7", "seven", "7 days", "seven days"]],
        ["How many hours are there in a day?", ["24", "twenty four", "24 hours", "twenty four hours"]],
        ["Which animal is known as the King of the Jungle?", "lion"],
        ["Name the National bird of India:", ["peacock", "the peacock"]]
    ]

    # Asking questions
    for q in questions:
        user_answer = input(q[0] + " ").lower()

        if isinstance(q[1], list):   # if multiple correct answers
            if user_answer in q[1]:
                print("Correct\n")
                count += 1
            else:
                print("Wrong\n")
                wrong += 1
        else:
            if user_answer == q[1]:
                print("Correct\n")
                count += 1
            else:
                print("Wrong\n")
                wrong += 1

    print("----------------------------------")
    print(f"Correct Answers: {count}")
    print(f"Wrong Answers  : {wrong}")
    print("----------------------------------")

    if count >= 4:
        print(f"Congratulations, You Won! Score: {count}/5")
    else:
        print(f"Better Luck Next Time. Score: {count}/5")

    print("----------------------------------\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thank you for playing. Goodbye.")
        break
