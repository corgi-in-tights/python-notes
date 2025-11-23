# 3.01.5 Conditional Expressions

# Conditional expressions evaluate to True or False
# They're used to make decisions in your code


# -----------------------------
# Comparison operators
# -----------------------------

x = 10
y = 20

x == y    # False (equal to)
x != y    # True (not equal to)
x < y     # True (less than)
x > y     # False (greater than)
x <= y    # True (less than or equal to)
x >= y    # False (greater than or equal to)


# -----------------------------
# Logical operators
# -----------------------------

# AND - both conditions must be True
# OR - at least one condition must be True
# NOT - flips True to False, or False to True

True and False   # False
True or False    # True
not True         # False


# -----------------------------
# Chaining conditions
# -----------------------------

age = 25
student = True
rich = False

# English: "Age is at least 18 AND is a student"
age >= 18 and student           # True

# English: "Rich OR a student"
rich or student                 # True

# English: "Age is at least 18 AND (rich OR a student)"
age >= 18 and (rich or student) # True

# English: "NOT rich AND is a student"
not rich and student            # True


# -----------------------------
# English to Python
# -----------------------------

# "Between 18 and 65"
# age >= 18 and age <= 65

# "Either weekend or holiday"
# is_weekend or is_holiday

# "Warm and NOT raining"
# temp > 70 and not raining

# "Score is 100 OR failed (below 60)"
# score == 100 or score < 60


# -----------------------------
# Python to English
# -----------------------------

# age < 13 or age > 65
# "Younger than 13 OR older than 65"

# score >= 90 and attendance > 0.8
# "Score is at least 90 AND attendance is above 80%"

# not (x > 10 and y > 10)
# "NOT (x is greater than 10 AND y is greater than 10)"

