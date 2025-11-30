# Question 1: List Methods - What Gets Printed?

# For each code block, write what gets printed or what the final value is.
# If there's an error, write "Error" and explain why.

# -----------------------------
# Block A
# -----------------------------

fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits.remove("banana")
print(fruits)

# What prints? _______________


# -----------------------------
# Block B
# -----------------------------

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()
last = numbers.pop()
print(last)
print(numbers)

# What prints? _______________


# -----------------------------
# Block C
# -----------------------------

letters = ["a", "b", "c", "b", "d"]
count = letters.count("b")
index = letters.index("b")
print(count)
print(index)

# What prints? _______________


# -----------------------------
# Block D
# -----------------------------

words = ["hello", "world"]
words.extend(["python", "code"])
words.insert(1, "amazing")
print(len(words))
print(words[1])

# What prints? _______________


# -----------------------------
# Block E
# -----------------------------

nums = [5, 2, 8, 1]
nums.reverse()
nums.append(10)
nums.remove(5)
print(nums)

# What prints? _______________


# -----------------------------
# Block F (Error!)
# -----------------------------

data = [1, 2, 3]
data.remove(5)
print(data)

# What happens? _______________
# Why? _______________