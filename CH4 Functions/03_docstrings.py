# 4.03 Docstrings

# Docstrings are special strings used to document your functions, classes, and modules.
# They help others (and your future self) understand what your code does.

# -----------------------------
# Writing a docstring
# -----------------------------

def greet(name):
    """
    Greets a person by name.
    Args:
        name (str): The name of the person to greet.
    Returns:
        None
    """
    print(f"Hello, {name}!")

# The docstring goes right after the function definition, inside triple quotes """ ... """
# It can be a single line or multiple lines.

# -----------------------------
# Why use docstrings?
# -----------------------------
# - They show up in help() and IDE tooltips
# - They make your code easier to use and maintain
# - They are a good habit for all your functions, even simple ones

# Example of a one-line docstring:
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

