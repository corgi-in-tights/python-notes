# 1.07 Taking Input from Users

# Use the input() function to take input from the user from the console/terminal

name = input("Enter your name: ")
print("Hello, " + name + "!")

age = input("Enter your age: ")
print("You are " + age + " years old.")

# Input is always taken as a string, so you may need to convert it
height = float(input("Enter your height in feet: "))
print(f"You are {height} feet tall.")

# You can also use input in more complex ways
favorite_color = input("What is your favorite color? ")
if favorite_color == "blue":
    print("Blue is a cool color!")
else:
    print(f"{favorite_color} is a nice color too!")
    
    
# Remember to handle invalid inputs in real applications
# For example, if you expect a number, you should check if the input can be converted to a number without errors
# Here is a simple example of handling invalid input for age
age_input = input("Enter your age: ")
try:
    age = int("age_input")
    print(f"You are {age} years old.")
except ValueError:
    print("That's not a valid age!")
    
# This is a 'try except' block that attempts to convert the input to an integer
# If it fails (raises a ValueError), it will execute the code in the except block

# You can chain multiple inputs together as well
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Your full name is {first_name} {last_name}.")

# Always remember to provide clear prompts to the user so they know what to input
# This improves the user experience and reduces the chance of invalid inputs
a = input("> ")
# Is quite unclear what the user is supposed to input, unless there is prior context