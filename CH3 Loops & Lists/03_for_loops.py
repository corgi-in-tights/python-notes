# 3.03 For Loops

# For loops iterate over sequences (like lists, strings, or ranges)


# -----------------------------
# For loop with range()
# -----------------------------

# Syntax: for variable in sequence:
#     code to repeat

# range(5) creates sequence: 0, 1, 2, 3, 4
for i in range(5):
    pass   # i takes values 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 6):
    pass   # i takes values 2, 3, 4, 5

# range(start, stop, step)
for i in range(0, 10, 2):
    pass   # i takes values 0, 2, 4, 6, 8


# -----------------------------
# For loop with lists
# -----------------------------

# Loop through each item in a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    pass   # fruit is "apple", then "banana", then "cherry"

# Loop with index
numbers = [10, 20, 30]
for i in range(len(numbers)):
    pass   # i is 0, 1, 2; numbers[i] is 10, 20, 30


# -----------------------------
# For loop with strings
# -----------------------------

# Loop through each character
word = "PYTHON"
for char in word:
    pass   # char is "P", then "Y", then "T", etc.


# -----------------------------
# For loop with break
# -----------------------------

# break exits the loop immediately
for i in range(10):
    if i == 5:
        break   # Stop when i equals 5
# Loop ends at i = 5, doesn't reach 6-9


# -----------------------------
# For loop with continue
# -----------------------------

# continue skips to the next iteration
for i in range(5):
    if i == 2:
        continue   # Skip when i is 2
    # This code won't run when i is 2


# -----------------------------
# Nested for loops
# -----------------------------

# Loop inside another loop
for i in range(3):
    for j in range(2):
        pass   # Runs 6 times total
# i=0, j=0; i=0, j=1; i=1, j=0; i=1, j=1; i=2, j=0; i=2, j=1


# -----------------------------
# Practical examples
# -----------------------------

# Sum all numbers in a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num   # total = 15

# Count items in a list
fruits = ["apple", "banana", "apple"]
apple_count = 0
for fruit in fruits:
    if fruit == "apple":
        apple_count += 1   # apple_count = 2

# Build a new list
numbers = [1, 2, 3, 4, 5]
doubled = []
for num in numbers:
    doubled.append(num * 2)   # doubled = [2, 4, 6, 8, 10]


# -----------------------------
# For vs While
# -----------------------------

# Use for when you know how many times to loop
for i in range(5):   # Loop exactly 5 times
    pass

# Use while when you loop until a condition changes
playing = True
while playing:   # Loop until playing is False
    if input("Quit? ") == "yes":
        playing = False
