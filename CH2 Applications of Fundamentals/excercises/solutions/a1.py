# Answer 1: Understanding If Statements

# 1. What happens in Version A if score = 95?
#    - It prints "A", then checks >= 80 (True), prints "B", then checks >= 70 (True), prints "C"
#    - Output: A B C (all three!)

# 2. What happens in Version B if score = 95?
#    - It prints "A", then STOPS checking the rest
#    - Output: A (only one!)

# 3. Which version is correct for a grading system? Why?
#    - Version B (elif) is correct
#    - A student should only get ONE grade, not multiple
#    - elif stops checking once a condition is True

# 4. When would you use multiple independent if statements instead?
#    - When you want to check multiple separate conditions
#    - Example: checking if someone is tall AND smart AND funny
#    - Each check is independent and all can be True at the same time