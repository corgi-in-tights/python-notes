# 1.05 Converting between data types

# So far, we’ve seen different data types:
#   - int      (e.g., 10, -3)
#   - float    (e.g., 3.14, 0.5)
#   - str      (e.g., "hello")
#   - bool     (True / False)
#
# Often we need to CONVERT (or "cast") between these types.

# You can always check a value's type using the type() function:
x = 10
print(type(x))  # <class 'int'>

y = "10"
print(type(y))  # <class 'str'>


# -----------------------------
# Converting strings to numbers
# -----------------------------

# We use int() to convert something to an integer
age_text = "25"
age_number = int(age_text)  # "25" -> 25 (string to int)

print("age_text:", age_text, "type:", type(age_text))
print("age_number:", age_number, "type:", type(age_number))

# We use float() to convert something to a floating-point number
pi_text = "3.14"
pi_number = float(pi_text)  # "3.14" -> 3.14 (string to float)

print("pi_text:", pi_text, "type:", type(pi_text))
print("pi_number:", pi_number, "type:", type(pi_number))


# --------------------------------
# Converting numbers to strings
# --------------------------------

# We use str() to convert a value to its string representation
score = 100
score_text = str(score)  # 100 -> "100"

print("score:", score, "type:", type(score))
print("score_text:", score_text, "type:", type(score_text))

# This is useful when building messages:
message = "Your score is " + score_text
print(message)


# -----------------------------
# Converting to booleans (bool)
# -----------------------------

# bool() converts values to True/False using simple rules:
print(bool(0))    # False
print(bool(1))    # True
print(bool(-5))   # True (any non-zero number becomes True)

print(bool(""))   # False (empty string)
print(bool("hi")) # True  (non-empty string)


# -------------------------------------------------
# When conversions FAIL: ValueError and exceptions
# -------------------------------------------------

# Not every string can be converted to a number.
# The following line would crash the program with a ValueError:
# bad_number = "twenty"
# int(bad_number)  # ValueError: invalid literal for int()

# To avoid crashing, we can CATCH the error using try/except.

text_value = "twenty"  # Pretend we got this from somewhere else in the program

try:
    number_value = int(text_value)  # This will FAIL for "twenty"
    print("Conversion succeeded:", number_value)
except ValueError:
    print("Conversion failed: cannot convert", text_value, "to an int.")

# General pattern:
#
# try:
#     # Code that might cause an error
#     risky_value = int("abc")
#     print("Converted:", risky_value)
# except ValueError:
#     # What to do if that specific error happens
#     print("There was a problem converting the value.")
#
# The program continues after the try/except block without crashing.


# ---------------------------------------
# Using conversion with conditions (if)
# ---------------------------------------

# Sometimes we need to compare numeric values, not strings.
# For example, imagine we have a string representing a temperature:

temperature_text = "30"      # string
temperature = int(temperature_text)  # convert to int first

if temperature > 25:
    print("It's warm!")
else:
    print("It's not that warm.")

# If we forgot to convert, we'd be comparing a string to a number,
# which is not what we want and can cause errors or unexpected behaviour.