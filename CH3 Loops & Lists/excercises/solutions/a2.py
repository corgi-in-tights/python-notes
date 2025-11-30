# Answer 2: While Loop with Break (Enhanced)

correct_password = "python123"
max_attempts = 3
attempts = 0

while True:
    user_password = input("Enter password: ")
    
    attempts += 1
    
    if user_password == correct_password:
        print("Access granted!")
        break
    else:
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong password, try again. Attempts remaining: {remaining}")
        
    if attempts >= max_attempts:
        print("Account locked! Too many failed attempts.")
        break

if attempts <= max_attempts and user_password == correct_password:
    print("Welcome!")
else:
    print("Please contact support.")