# 3.02 While Loops

# While loops repeat code as long as a condition is True
# Note: if your code ever goes stuck in an infinite loop,
# you can usually stop it with Ctrl + C

# -----------------------------
# Basic while loop
# -----------------------------

# Syntax: while condition:
#     code to repeat

count = 0
while count < 5:
    count += 1   # Increment count each time
# After loop ends, count = 5

# The loop checks the condition BEFORE each iteration
# If the condition is False from the start, the loop never runs


# -----------------------------
# While loop with break
# -----------------------------

# A break is a way to exit the loop early usually conditionally

# break exits the loop immediately (i.e. moves to the end)

count = 0
while True:   # Infinite loop
    count += 1
    if count >= 5:
        break   # Exit when count reaches 5
# count = 5

# General rule of thumb is:
# Use break to exit loops based on conditions inside the loop
# Avoid using break for normal loop control

# We can use break in conjunction with input to exit loops
# based on user input
# i.e. force them to provide a specific answer

while True:
    res = input("Say 'yes': ")
    if res == "yes":
        break


# -----------------------------
# While loop with continue
# -----------------------------

# continue skips to the next iteration

count = 0
while count < 5:
    count += 1
    if count == 3:
        continue   # Skip when count is 3
    # This code won't run when count is 3


# -----------------------------
# Practical example: User input
# -----------------------------

# Keep asking until user says "yes"
playing = True
while playing:
    res = input("Say 'yes': ")
    if res == "yes":
        playing = False   # Exit condition
# Loop ends when playing becomes False


