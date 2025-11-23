# Answer 1: Conditional Logic Explanations

# -----------------------------
# Answer A: Independence
# -----------------------------

# Output: A B C (all three print)

# Explanation:
# - Each if statement is independent - they ALL run
# - First if: 15 > 10 is True, prints "A"
# - Second if: 15 > 5 is True, prints "B"
# - Third if: 15 > 0 is True, prints "C"
# - To print only "A", use elif instead of the second/third if


# -----------------------------
# Answer B: Precedence
# -----------------------------

# 1. not True or False
#    - not is evaluated first: not True = False
#    - Then or: False or False = False

# 2. True or False and False
#    - and is evaluated before or
#    - False and False = False
#    - True or False = True

# 3. 10 > 5 and not False or 3 < 2
#    - Comparisons first: 10 > 5 = True, 3 < 2 = False
#    - not next: not False = True
#    - and next: True and True = True
#    - or last: True or False = True


# -----------------------------
# Answer C: Combined Conditions
# -----------------------------

# The bug: Missing parentheses makes the condition ambiguous

# Current interpretation (due to precedence):
# (age >= 18 and income >= 25000) or income >= 50000
# This approves age=17, income=60000 because income >= 50000 is True

# What it SHOULD be (both conditions required):
# age >= 18 and (income >= 25000 or income >= 50000)
# This requires age >= 18 AND at least one income condition

# Fixed code:
# if age >= 18 and (income >= 25000 or income >= 50000):
#     print("Approved")
