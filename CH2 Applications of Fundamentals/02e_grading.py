# 2.02 Exercise: Grade Calculator

score = float(input("Enter score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

passed = score >= 60  # Boolean: True or False

print(f"Score: {score} -> Grade: {grade}")
print(f"Passed: {passed}")


# -----------------------------
# YOUR TURN: Calculate average of 3 tests
# -----------------------------

# 1. Ask for 3 test scores
# 2. Calculate the average
# 3. Print the average and letter grade

# Write your solution below:
