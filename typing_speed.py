import time

print("\n--- Typing Speed Tester ---")
text = "Python is a powerful programming language"

print("\nType the following sentence:")
print(text)

start = time.time()
user = input("\nStart typing here: ")
end = time.time()

time_taken = round(end - start, 2)
words = len(text.split())
wpm = round((words / time_taken) * 60, 2)  # Words per minute

print(f"\nTime Taken: {time_taken} seconds")
print(f"Typing Speed: {wpm} WPM")

if user == text:
    print("Accuracy: 100%")
else:
    correct_chars = sum(1 for i,j in zip(user, text) if i == j)
    accuracy = round((correct_chars / len(text)) * 100, 2)
    print(f"Accuracy: {accuracy}%")
