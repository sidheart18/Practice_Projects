import random

responses = [
    "Interesting... tell me more.",
    "I agree with that.",
    "Why do you think so?",
    "That sounds fun.",
    "Not sure, but I like the confidence.",
    "Let me think about that...",
    "I didn't expect that answer!"
]

print("\n--- Fake Chat Generator ---")
print("Type 'bye' to end the chat\n")

while True:
    user = input("You: ")
    
    if user.lower() == "bye":
        print("Bot: Talk to you later.")
        break

    print("Bot:", random.choice(responses))
