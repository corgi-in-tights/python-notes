# Question 2: While Loop with Break (Enhanced)

# Fill in the missing code to complete the password checker.
# The loop should keep asking for a password until the correct one is entered.
# Use break to exit the loop when correct.
# Add attempt tracking and lockout feature.

correct_password = "python123"
max_attempts = 3
attempts = 0

while True:
    # TODO: Ask user to enter password
    user_password = ""  # Fill this in
    
    # TODO: Increment attempts counter
    
    # TODO: Check if password is correct
    # If correct, print "Access granted!" and break
    # If incorrect, print "Wrong password, try again."
    # Also print how many attempts remain
    
    # TODO: Check if max attempts reached
    # If so, print "Account locked! Too many failed attempts." and break
    

if attempts <= max_attempts and user_password == correct_password:
    print("Welcome!")
else:
    print("Please contact support.")


# Example output:
# Enter password: hello
# Wrong password, try again. Attempts remaining: 2
# Enter password: test
# Wrong password, try again. Attempts remaining: 1
# Enter password: wrong
# Account locked! Too many failed attempts.
# Please contact support.