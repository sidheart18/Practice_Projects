import random

words = ["python", "water", "school", "bottle", "mobile", "laptop", "garden", "animal"]
print("\n--- Word Scramble Game ---")

score = 0
for i in range(5):
    word = random.choice(words)
    scrambled = "".join(random.sample(word, len(word)))
    
    print(f"\nScrambled word: {scrambled}")
    guess = input("Your guess: ").lower()

    if guess == word:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong, the correct word was: {word}")

print(f"\nGame Over. Your Score: {score}/5")
