# 1.04 If Conditions

# If conditions allow you to execute code based on certain conditions
age = 20
if age >= 18:  # Notice how we use a comparison operator here to check if they are over or equal to 18
    
    # The code inside the if block runs only if the condition is True
    print("You are an adult.")
    # The indentation (4 spaces) is important in Python to define blocks of code
    # That is how it knows "THIS SHOULD ONLY EXECUTE IF THE CONDITION IS TRUE"
    
# You can also use else to run code when the other conditions are not met
# i.e.
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# You can chain multiple conditions using elif (else if)
age = 70
if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
    
# You can also combine conditions using logical operators (and, or, not)
temperature = 75
is_sunny = True
if temperature > 70 and is_sunny:
    # It is hot and sunny
    print("It's a nice day for outdoor activities!")
if temperature < 50 or not is_sunny:
    # It is cold or not sunny
    print("You might want to stay indoors today.")
    
# Notice how both if conditions are 'independant' of each other, as in, both can run if their conditions are met
# But really they don't because they rely on antithetical conditions (hot vs cold)

# Nested if conditions
age = 25
has_id = True
if age >= 18:
    # Everything in this block only runs if age >= 18
    if has_id:
        print("You can enter the club.")
    else:
        print("You need to show your ID to enter.")
        
        