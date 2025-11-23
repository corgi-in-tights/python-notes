# 3.01 Introduction to Lists

# Lists are ordered collections that can hold multiple values


# -----------------------------
# Creating lists
# -----------------------------

# Empty list
empty = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]

# A list can hold mixed data types in Python:
mixed = [1, "hello", 3.14, True]
# Always be mindful of the types you are working with!


# -----------------------------
# Accessing list items
# -----------------------------

# Syntax: list[index]
# Index starts at 0, just like strings

fruits = ["apple", "banana", "cherry"]

fruits[0]   # "apple" (first item)
fruits[1]   # "banana" (second item)
fruits[2]   # "cherry" (third item)

# Negative indexing from the end
fruits[-1]  # "cherry" (last item)
fruits[-2]  # "banana" (second to last)


# -----------------------------
# List slicing
# -----------------------------

# Syntax: list[start:end]

numbers = [10, 20, 30, 40, 50]

numbers[1:4]   # [20, 30, 40] (indices 1, 2, 3)
numbers[:3]    # [10, 20, 30] (from start to 3)
numbers[2:]    # [30, 40, 50] (from 2 to end)
numbers[:]     # [10, 20, 30, 40, 50] (entire list)


# -----------------------------
# Modifying lists
# -----------------------------

# These are 'list methods', we'll cover methods in more detail later
# but the basic ones are to add and remove items in the list programmatically

# Change an item
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"  # ["apple", "blueberry", "cherry"]

# Add to end
fruits.append("date")    # ["apple", "blueberry", "cherry", "date"]

# Remove an item
fruits.remove("apple")   # ["blueberry", "cherry", "date"]


# -----------------------------
# List operations
# -----------------------------

# Length
len([1, 2, 3, 4])   # 4

# Check if item exists
"apple" in ["apple", "banana"]   # True
"grape" in ["apple", "banana"]   # False

# Concatenation
[1, 2] + [3, 4]   # [1, 2, 3, 4]

# Repetition
[1, 2] * 3   # [1, 2, 1, 2, 1, 2]


# -----------------------------
# Practical example
# -----------------------------

# Shopping list
shopping = ["milk", "eggs", "bread"]

# Add items
shopping.append("butter")
shopping.append("cheese")

# Check if we need apples
if "apples" not in shopping:
    shopping.append("apples")

# Number of items
total_items = len(shopping)  # 6
