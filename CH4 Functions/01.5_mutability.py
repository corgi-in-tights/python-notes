# 4.01.5 Mutability Refresher

# In Python, data types are either mutable (can be changed) or immutable (cannot be changed).
# This affects how variables behave when passed to functions or modified.

# -----------------------------
# Immutable types
# -----------------------------
# int, float, str, tuple, bool

x = 10
s = "hello"
t = (1, 2, 3)

# You cannot change these objects in place:
# x[0] = 5  # Error
# s[0] = 'H'  # Error
# t[0] = 9  # Error

# Any operation that seems to "change" them actually creates a new object:
s2 = s.upper()  # s2 is 'HELLO', s is still 'hello'

# -----------------------------
# Mutable types
# -----------------------------
# list, dict

mylist = [1, 2, 3]
mylist[0] = 99  # This works

mydict = {'a': 1}
mydict['b'] = 2  # This works

# -----------------------------
# Why does this matter?
# -----------------------------
# If you pass a mutable object to a function, it can be changed inside the function.
# If you pass an immutable object, it cannot be changed inside the function.

# See the 'Passing Parameters' section in 02_scoping.py for examples!
