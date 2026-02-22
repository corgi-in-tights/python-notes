# 5.02 Exercise: Math Formula Evaluator (Function Version)

# Complete the three functions below so the main code works!

def get_formula_input():
	"""
	Ask the user to enter a math formula and return it as a string.
	Example: '2+3*4'
	"""
	# TODO: Write this function
	pass

def is_formula_safe(formula):
	"""
	Return True if the formula only contains safe characters (digits, +, -, *, /, (, ), ., and spaces).
	Otherwise, return False.
	"""
	# TODO: Write this function
	pass

def evaluate_formula(formula):
	"""
	Evaluate the formula string and return the result.
	Use eval().
	"""
	# TODO: Write this function
	pass

# Main code (do not change)
print("Welcome to the Math Formula Evaluator!")
print("You can enter any arithmetic expression (e.g., 2+3*4, (5-2)**2/3, etc.)")

formula = get_formula_input()

try:
	if not is_formula_safe(formula):
		raise ValueError("Invalid characters in formula.")
	result = evaluate_formula(formula)
	print(f"Result: {result}")
except Exception as e:
	print(f"Error: {e}")
