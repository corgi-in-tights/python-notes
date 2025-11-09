# 1.02 Printing to console

# To open the terminal in vscode, go to View -> Terminal, 
# or use the shortcut `Control + Shift + ` (backtick)

# Print a simple string
print("Hello, World!")

# Print multiple items
name = "Alice"
age = 30
print("Name:", name, "Age:", age) # Output: Name: Alice Age: 30
# Notice how commas add spaces between items automatically

# Print formatted strings using f-strings (Python 3.6+)
height = 5.7
print(f"{name} is {age} years old and {height} feet tall.")

# Print with special characters
print("This is a line.\nThis is another line.")  # New line
print("Column1\tColumn2\tColumn3")  # Tab spaces

# Blank line for better readability in output
print()

# Print without a newline at the end
print("This is printed on the same line.", end=" ")
print("See?")