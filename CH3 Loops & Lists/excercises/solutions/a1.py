# Answer 1: List Methods - What Gets Printed?

# -----------------------------
# Block A
# -----------------------------

# Output: ['apple', 'cherry', 'date']
# Explanation:
# - append("date") adds "date" to end
# - remove("banana") removes "banana"
# - Result: ['apple', 'cherry', 'date']


# -----------------------------
# Block B
# -----------------------------

# Output:
# 9
# [1, 1, 2, 3, 4, 5]

# Explanation:
# - sort() arranges in order: [1, 1, 2, 3, 4, 5, 9]
# - pop() removes and returns last item (9)
# - Remaining list: [1, 1, 2, 3, 4, 5]


# -----------------------------
# Block C
# -----------------------------

# Output:
# 2
# 1

# Explanation:
# - count("b") returns 2 ("b" appears twice)
# - index("b") returns 1 (first occurrence at index 1)


# -----------------------------
# Block D
# -----------------------------

# Output:
# 5
# amazing

# Explanation:
# - extend adds ["python", "code"] to end: ["hello", "world", "python", "code"]
# - insert(1, "amazing") adds "amazing" at index 1: ["hello", "amazing", "world", "python", "code"]
# - len() returns 5
# - words[1] is "amazing"


# -----------------------------
# Block E
# -----------------------------

# Output: [1, 8, 2, 10]

# Explanation:
# - reverse() reverses to [1, 8, 2, 5]
# - append(10) adds 10 to end: [1, 8, 2, 5, 10]
# - remove(5) removes first 5: [1, 8, 2, 10]


# -----------------------------
# Block F (Error!)
# -----------------------------

# Error: ValueError: list.remove(x): x not in list
# Why: Trying to remove 5, but 5 doesn't exist in the list [1, 2, 3]