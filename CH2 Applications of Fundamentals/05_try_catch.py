# 2.05 Try-Catch (Error Handling)

# Sometimes code can fail - try-catch helps you handle errors gracefully


# -----------------------------
# Common errors
# -----------------------------
"""
SyntaxError - code is written wrong
print("hello"   # Missing closing parenthesis

NameError - using undefined variable
print(x)   # x doesn't exist

TypeError - wrong type for operation
"hello" + 5   # Can't add string and number

ValueError - right type, wrong value
int("abc")   # Can't convert "abc" to number

IndexError - accessing invalid index
word = "hi"
word[5]   # Only indices 0 and 1 exist

ZeroDivisionError - dividing by zero
10 / 0
"""

# -----------------------------
# Try-Except basics
# -----------------------------

# Syntax: try to do something, if it fails, handle the error

try:
    result = 10 / 0
    print(result)
except Exception:
    print("Something went wrong!")

# The code in except runs only if an error occurs


# -----------------------------
# Catching specific errors
# -----------------------------

# Better to catch specific error types

try:
    num = int("abc")
except ValueError:
    print("That's not a valid number!")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")


# -----------------------------
# Try-Catch with user input
# -----------------------------

# Most common use: converting input to numbers

age_input = input("Enter your age: ")
try:
    age = int(age_input)
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number!")

# Without try-catch, invalid input would crash the program


# -----------------------------
# Multiple error types
# -----------------------------

# Handle different errors differently

user_input = input("Enter a number: ")
try:
    number = float(user_input)
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a number!")
except ZeroDivisionError:
    print("Can't divide by zero!")


# -----------------------------
# Try-Except-Else
# -----------------------------

# Else runs if NO error occurs

try:
    score = int(input("Enter score: "))
except ValueError:
    print("Invalid number!")
else:
    print(f"Score recorded: {score}")
    # This only runs if conversion succeeded
