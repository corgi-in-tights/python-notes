# 2.03 String Operations

# Strings are sequences of characters that you can access and manipulate


# -----------------------------
# String indexing
# -----------------------------

# Access individual characters using square brackets []
# Index starts at 0

word = "PYTHON"

word[0]   # "P" (first character)
word[1]   # "Y" (second character)
word[5]   # "N" (last character)

# Negative indexing counts from the end
word[-1]  # "N" (last character)
word[-2]  # "O" (second to last)


# -----------------------------
# String slicing
# -----------------------------

# Get a substring using [start:end]
# The end index is NOT included

word = "PYTHON"

word[0:3]   # "PYT" (characters 0, 1, 2)
word[2:5]   # "THO" (characters 2, 3, 4)
word[:3]    # "PYT" (from start to 3)
word[3:]    # "HON" (from 3 to end)


# -----------------------------
# String operations
# -----------------------------

# Concatenation (joining strings)
first = "Hello"
last = "World"
full = first + " " + last   # "Hello World"

# Repetition
echo = "ha" * 3   # "hahaha"

# Length
len("PYTHON")   # 6

# Check if substring exists
"TH" in "PYTHON"    # True
"XY" in "PYTHON"    # False


# -----------------------------
# String methods
# -----------------------------

text = "hello world"

text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.capitalize()   # "Hello world"

# Replace text
text.replace("world", "python")   # "hello python"

# Split into a list (we'll learn lists later)
text.split()   # ["hello", "world"]
