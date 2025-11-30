# 1.03 Operators

# Operators are special symbols that perform operations on variables and values
# Here are some common types of operators in Python:

# -----------------------------
# Arithmetic Operators
# -----------------------------

# These take in two basic data types (integers or floats) and return a single value (which can be an integer or float)
# If a float is used in the operation, the result will *usually* be a float
a = 10
b = 3

a + b           # 13 - Addition
a - b           # 7 - Subtraction
a * b           # 30 - Multiplication
a / b           # 3.333... - Division
a // b          # 3 - Floor Division, rounds *down* to the nearest whole number
a % b           # 1 - Modulus, returns the remainder between division
a ** b          # 1000 - Exponentiation, a raised to the bth power
    
# -----------------------------
# Comparison Operators
# -----------------------------

# These compare two values and return a Boolean (True or False) *always*
# Essentially, you can answer simple yes or no questions, or much more complex ones by breaking things down

a == b          # False - Equal to
a != b          # True - Not equal to
a > b           # True - Greater than
a < b           # False - Less than
a >= b          # True - Greater than or equal to
a <= b          # False - Less than or equal to


# -----------------------------
# Logical Operators
# -----------------------------

# These combine multiple Boolean values and return a single Boolean value
# They are useful for building complex conditions
# "This is a dog AND it is brown"
# "I have a cat OR (I have a dog AND it is black)" is akin to: has_cat or (has_dog and dog_color == "black")
x = True
y = False

x and y         # False - Logical AND
x or y          # True - Logical OR
not x           # False - Logical NOT

# You can combine comparison operators with logical operators
(a > b) and (x or y)  # True - Combined


# -----------------------------
# Assignment Operators
# -----------------------------

# Shortcuts for assigning values to variables
c = 5           # Initial value: 5
c += 2          # Equivalent to c = c + 2, now c = 7
c *= 3          # Equivalent to c = c * 3, now c = 21
c -= 4          # Equivalent to c = c - 4, now c = 17
c /= 2          # Equivalent to c = c / 2, now c = 8.5


# -----------------------------
# Combining multiple operators
# -----------------------------

# Arithmetic and comparison
x = 10
y = 20
x + 5 > y       # False (15 > 20)
x * 2 == y      # True (20 == 20)

# Comparison and logical
age = 25
score = 85
age >= 18 and score >= 60       # True (both conditions are True)
age < 18 or score >= 90         # False (both conditions are False)

# All together
price = 100
discount = 20
has_coupon = True
(price - discount) < 90 and has_coupon  # True (80 < 90 and True)


# -----------------------------
# Operator precedence
# -----------------------------

# Order of operations (highest to lowest):
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
# 5. Comparison ==, !=, <, >, <=, >=
# 6. not
# 7. and
# 8. or

# Examples:
2 + 3 * 4       # 14 (multiplication first, then addition)
(2 + 3) * 4     # 20 (parentheses first)
10 > 5 and 20 > 15  # True (comparisons first, then and)
not True or False   # False (not first, then or)

# Use parentheses for clarity!
5 + 3 > 6 and 10 < 20       # Works, but confusing
(5 + 3 > 6) and (10 < 20)   # Clearer
