# game.py

# 1. Import the module you need for randomness
import random
# 2. A list of at least 5 words
words = ["Eclipse", "Volcano", "Photosynthesis", "Guitar", "Gravity"]

# 3. Pick one word at random from the list
secret_word = random.choice(words)

# 4. Build the display: one "_" per letter
display = "_ " * len(secret_word)


# 5. Print it
print(display)