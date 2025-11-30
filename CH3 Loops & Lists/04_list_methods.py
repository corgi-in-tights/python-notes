# 3.04 List Methods

# List methods are functions that belong to lists and modify or query them


# -----------------------------
# Adding items
# -----------------------------

# append() - add item to end
fruits = ["apple", "banana"]
fruits.append("cherry")     # ["apple", "banana", "cherry"]

# insert() - add item at specific position
fruits.insert(1, "orange")  # ["apple", "orange", "banana", "cherry"]
# Syntax: list.insert(index, item)

# extend() - add multiple items
fruits.extend(["grape", "mango"])  # ["apple", "orange", "banana", "cherry", "grape", "mango"]


# -----------------------------
# Removing items
# -----------------------------

# remove() - remove first occurrence of value
fruits = ["apple", "banana", "apple", "cherry"]
fruits.remove("apple")      # ["banana", "apple", "cherry"]
# Only removes the FIRST "apple"

# pop() - remove and return item at index
fruits = ["apple", "banana", "cherry"]
last = fruits.pop()         # last = "cherry", fruits = ["apple", "banana"]
first = fruits.pop(0)       # first = "apple", fruits = ["banana"]

# clear() - remove all items
fruits.clear()              # []


# -----------------------------
# Finding items
# -----------------------------

# index() - find position of first occurrence
fruits = ["apple", "banana", "cherry"]
pos = fruits.index("banana")  # pos = 1

# count() - count occurrences
numbers = [1, 2, 3, 2, 4, 2]
count = numbers.count(2)    # count = 3


# -----------------------------
# Sorting and reversing
# -----------------------------

# sort() - sort in place (modifies the list)
numbers = [3, 1, 4, 2]
numbers.sort()              # [1, 2, 3, 4]
numbers.sort(reverse=True)  # [4, 3, 2, 1]

# reverse() - reverse in place
numbers = [1, 2, 3, 4]
numbers.reverse()           # [4, 3, 2, 1]


# -----------------------------
# Common errors
# -----------------------------

# ValueError: item not in list
# fruits = ["apple", "banana"]
# fruits.remove("cherry")   # Error! "cherry" not in list

# IndexError: pop from empty list
# empty = []
# empty.pop()               # Error! Can't pop from empty list

# ValueError: item not in list
# fruits = ["apple", "banana"]
# fruits.index("cherry")    # Error! "cherry" not in list


# -----------------------------
# Practical use cases
# -----------------------------

# Build a shopping list
shopping = []
shopping.append("milk")
shopping.append("eggs")
shopping.append("bread")
# shopping = ["milk", "eggs", "bread"]

# Remove bought items
shopping.remove("eggs")     # ["milk", "bread"]

# Check if item exists before removing
if "milk" in shopping:
    shopping.remove("milk")

# Sort names alphabetically
names = ["Charlie", "Alice", "Bob"]
names.sort()                # ["Alice", "Bob", "Charlie"]

# Count duplicates
scores = [100, 85, 100, 90, 100]
perfect_scores = scores.count(100)  # 3
