# 2.03 Exercise: Wordle Lite

# A simple word guessing game that 
# checks if letters are in the right position

# -----------------------------
# YOUR TURN: Complete the game!
# -----------------------------

secret = "PYTHON"
guess = input("Guess a 5-letter word: ").upper()

# Check position 1
if guess[0] == secret[0]:
    print("Position 1: Yes")
elif guess[0] in secret:
    print("Position 1: Maybe")
else:
    print("Position 1: No")

# Check position 2
if guess[1] == secret[1]:
    print("Position 2: Yes")
elif guess[1] in secret:
    print("Position 2: Maybe")
else:
    print("Position 2: No")
    
    
# Now YOU write the code to check positions 3, 4, and 5

# If the word is guessed correctly, print "Congratulations! 
