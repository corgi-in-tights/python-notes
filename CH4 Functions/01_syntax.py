# 4.01 Function Syntax

# Functions are reusable blocks of code that perform a specific task.
# They help organize code, avoid repetition, and make programs easier to read and maintain.

# -----------------------------
# Defining a function
# -----------------------------

def greet():
    print("Hello!")

# 'def' starts the function definition
# 'greet' is the function name
# Parentheses () are required, even if there are no parameters
# The code inside the function is indented

# -----------------------------
# 'Invoking' or 'Calling' a function
# -----------------------------

greet()  # Output: Hello!

# You can call a function as many times as you want

greet()
greet()

# -----------------------------
# Function with parameters
# -----------------------------

# A parameter is a variable that the function can use to receive input when it's called
# In this case, 'name' is a parameter that takes the value passed when calling the

def greet_person(name):
    print("Hello,", name)

greet_person("Alice")  # Output: Hello, Alice

greet_person("Bob")    # Output: Hello, Bob


# -----------------------------
# Function with a return value
# -----------------------------

def average(list_of_numbers):
    total = 0
    for num in list_of_numbers:
        total = add(total)
    count = len(list_of_numbers)
    return total / count

def add(a, b):
    return a + b

result = add(2, 3)  # result is 5
print(result)

# 'return' sends a value back to where the function was called
# If no return statement, the function returns None by default

# This can also be used to end a function early
def check_positive(num):
    if num <= 0:
        return "Not positive"
    return "Positive"
print(check_positive(5))   # Output: Positive
print(check_positive(-2))  # Output: Not positive