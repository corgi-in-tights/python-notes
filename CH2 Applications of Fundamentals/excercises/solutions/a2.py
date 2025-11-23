# Answer 2: String Operations Practice

first = input("Enter first name: ")
last = input("Enter last name: ")

# Build email using concatenation and .lower()
email = first.lower() + "_" + last.lower() + "@email.com"

print(f"Email: {email}")
print(f"First character: {email[0]}")
