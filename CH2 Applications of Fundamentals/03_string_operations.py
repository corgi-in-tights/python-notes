# 2.03 String Operations

# Strings are sequences of characters that you can access and manipulate


# -----------------------------
# String indexing
# -----------------------------

# Syntax: string[index]
# This is how we access individual characters in a string

# Access individual characters using square brackets []
# Index starts at 0

word = "PYTHON"

word[0]   # "P" (first character)
word[1]   # "Y" (second character)
word[5]   # "N" (last character)

# Negative indexing counts from the end
word[-1]  # "N" (last character)
word[-2]  # "O" (second to last)
word[-6]  # "P" (same as word[0])

# Using indexing in practice
name = "Alice"
first_letter = name[0]  # "A"
last_letter = name[-1]  # "e"


# -----------------------------
# String slicing
# -----------------------------

# Syntax: string[start:end]
# Get a substring using [start:end]
# The end index is NOT included

word = "PYTHON"

word[0:3]   # "PYT" (characters 0, 1, 2)
word[2:5]   # "THO" (characters 2, 3, 4)
word[:3]    # "PYT" (from start to 3)
word[3:]    # "HON" (from 3 to end)
word[:]     # "PYTHON" (entire string)

# Using slicing in practice
email = "user@example.com"
username = email[:4]  # "user"
domain = email[5:]    # "example.com"


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

# Case conversion
text.upper()        # "HELLO WORLD"
text.lower()        # "hello world"
text.capitalize()   # "Hello world"
text.title()        # "Hello World"

# Checking content
text.startswith("hello")   # True
text.endswith("world")     # True
text.isalpha()             # False (has a space)
"123".isdigit()            # True

# Modifying strings
text.replace("world", "python")   # "hello python"
"  hello  ".strip()               # "hello" (removes whitespace)

# Split into a list (we'll learn lists later)
text.split()   # ["hello", "world"]
"a,b,c".split(",")   # ["a", "b", "c"]


# -----------------------------
# Methods vs Functions
# -----------------------------

# Functions are called directly: function(value)
len("PYTHON")      # 6 - function
type("hello")      # <class 'str'> - function
str(123)           # "123" - function

# Methods are called on objects: object.method()
"PYTHON".lower()   # "python" - method
"hello".upper()    # "HELLO" - method
"test".replace("t", "b")  # "besb" - method

# Both do things, but methods belong to specific types (like strings)
# Functions are more general and can work with different types

# The syntax for a method is ALWAYS:
# object.method(arguments)

# While for functions it is:
# function(arguments)