# 1.06 Data Type Interactions

# Data type interactions refer to how different data types behave
# when combined or used together in operations.

# -----------------------------
# Strings and Strings
# -----------------------------

# When you add two strings using the + operator, Python concatenates them.
s1 = "hot"
s2 = "dog"

s3 = s1 + s2   # "hotdog"
# You can also insert a space manually if needed:
s4 = s1 + " " + s2   # "hot dog"

# Multiplying a string by an integer repeats it that many times:
s5 = "ha" * 3   # "hahaha"


# -----------------------------
# Numbers and Numbers
# -----------------------------

# Integers and floats can freely interact in arithmetic expressions.
x = 5       # int
y = 2.0     # float

z = x + y   # Result: 7.0 (float)
# The presence of a float converts the result to a float automatically.

# Similarly:
x * y       # 10.0
x / 2       # 2.5 (float even if both are ints)
x // 2      # 2  (floor division forces integer result if both are ints)


# -----------------------------
# Strings and Numbers
# -----------------------------

# You cannot directly add or combine strings and numbers:
# "age: " + 25   # TypeError: can only concatenate str (not "int") to str

# To combine them, convert the number to a string:
age = 25
text = "Age: " + str(age)   # "Age: 25"

# Or use f-strings (recommended in modern Python, see 1.02):
text2 = f"Age: {age}"       # "Age: 25"


# -----------------------------
# Booleans and Numbers
# -----------------------------

# Booleans behave like numbers:
#   True  -> 1
#   False -> 0
# which means:

if 0:
    print("This won't print because False == 0.")
if 1:
    print("This will print because True == 1.")


a = True
b = False

a + b       # 1 (1 + 0)
a * 10      # 10
b * 5       # 0

# This can be useful in conditions or quick counts:
count = True + True + False  # 2


# -----------------------------
# Mixing everything
# -----------------------------

# Python generally only allows mixing types when it knows what to do
# If not, you’ll get a TypeError and need to explicitly convert one side

# Examples:
10 + "5"                  # TypeError
int("5") + 10             # 15
"Total: " + str(10 + 5)   # "Total: 15"

# General rule of thumb is it tends to be intuitive and explicit
# When in doubt, convert types explicitly using int(), float(), str(), or bool().

# For example, you cannot subtract strings because it is not clear what that means:
# "hello" - "he"   could mean a lot of things
# while
# "hello" * 2      is quite intuitive as it resolves to "hello" + "hello" = "hellohello"