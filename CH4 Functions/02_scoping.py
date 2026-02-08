# 4.02 Function Scoping

# Scope refers to where variables can be accessed in your code.
# In Python, variables defined inside a function are LOCAL to that function.

# -----------------------------
# Local scope
# -----------------------------

def show_number():
    x = 10  # x is local to show_number
    print("Inside function, x =", x)

show_number()  # Output: Inside function, x = 10
# print(x)  # Error! x is not defined outside the function

# -----------------------------
# Global scope
# -----------------------------

y = 5  # y is a 'global' variable

def print_y():
    print("Inside function, y =", y)

print_y()  # Output: Inside function, y = 5
print("Outside function, y =", y)  # Output: Outside function, y = 5

# -----------------------------
# Nested functions and nonlocal
# -----------------------------

def outer():
    a = "outer variable"
    def inner():
        nonlocal a  # refers to 'a' in the nearest enclosing function
        a = "changed by inner"
        print("Inside inner, a =", a)
    inner()
    print("Inside outer, a =", a)

outer()


# -----------------------------
# Passing Parameters
# -----------------------------

# When you pass a variable to a function, Python passes a reference to the object.

# For immutable types (int, float, str, tuple), 
# changes inside the function do NOT affect the original.

# For mutable types (list, dict), 
# changes inside the function CAN affect the original.

def try_to_change_number(n):
    n = 99
    print("Inside function, n =", n)

num = 5
try_to_change_number(num)
print("Outside function, num =", num)  # num is still 5

def try_to_change_list(lst):
    lst.append(42)
    print("Inside function, lst =", lst)

mylist = [1, 2, 3]
try_to_change_list(mylist)
print("Outside function, mylist =", mylist)  # mylist is changed

# Summary:
# - Variables inside a function are local by default
# - Use 'global' to modify global variables
# - Use 'nonlocal' to modify variables in an enclosing function
# - Immutable arguments (int, str, etc.) are not changed by the function
# - Mutable arguments (list, dict, etc.) can be changed by the function
