# 1.03 Operators

# Operators are special symbols that perform operations on variables and values
# Here are some common types of operators in Python:

# Arithmetic Operators
# These take in two basic data types (integers or floats) and return a single value (which can be an integer or float)
# If a float is used in the operation, the result will *usually* be a float
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Floor Division:", a // b)   # Floor Division, rounds *down* to the nearest whole number
print("Modulus:", a % b)           # Modulus, returns the remainder between division
print("Exponentiation:", a ** b)   # Exponentiation, a raised to the bth power


# Comparison Operators
# These compare two values and return a Boolean (True or False) *always*
# Essentially, you can answer simple yes or no questions, or much more complex ones by breaking things down
print("\nComparison Operators:")
print("Equal to:", a == b)         # Equal to
print("Not equal to:", a != b)     # Not equal to
print("Greater than:", a > b)      # Greater than
print("Less than:", a < b)         # Less than
print("Greater than or equal to:", a >= b)  # Greater than or equal to
print("Less than or equal to:", a <= b)     # Less than or equal to


# Logical Operators
# These combine multiple Boolean values and return a single Boolean value
# They are useful for building complex conditions
# "This is a dog AND it is brown"
# "I have a cat OR (I have a dog AND it is black)" is akin to: has_cat or (has_dog and dog_color == "black")
x = True
y = False
print("\nLogical Operators:")
print("Logical AND:", x and y)     # Logical AND
print("Logical OR:", x or y)       # Logical OR
print("Logical NOT:", not x)       # Logical NOT

# You can combine comparison operators with logical operators
print("Combined:", (a > b) and (x or y))  # Combined


# Assignment Operators
# Shortcuts for assigning values to variables
print("\nAssignment Operators:")
c = 5
print("Initial value of c:", c)
c += 2  # Equivalent to c = c + 2
c *= 3  # Equivalent to c = c * 3
c -= 4  # Equivalent to c = c - 4
c /= 2  # Equivalent to c = c / 2
print("Final value of c after compound assignments:", c)