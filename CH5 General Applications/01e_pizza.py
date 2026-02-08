# 5.01 Exercise: Pizza Order Calculator

# This example uses functions and loops to build a simple pizza order calculator.
# The user can order multiple pizzas, choose sizes, and get a total bill.

# -----------------------------
# Function to calculate price based on size
# -----------------------------
def get_pizza_price(size):
    if size == 'S':
        return 8
    elif size == 'M':
        return 10
    elif size == 'L':
        return 12
    else:
        return 0  # Invalid size

# -----------------------------
# Main order loop
# -----------------------------

total = 0
order_count = int(input("How many pizzas would you like to order? "))

for i in range(order_count):
    print(f"\nPizza #{i+1}")
    size = input("Choose size (S/M/L): ").upper()
    price = get_pizza_price(size)
    if price == 0:
        print("Invalid size, skipping this pizza.")
        continue
    total += price
    print(f"Added a {size} pizza for ${price}.")

print("\nOrder complete!")
print(f"Total bill: ${total}")

# -----------------------------
# YOUR TURN: Try this!
# -----------------------------
# 1. Add toppings (e.g., $2 for extra cheese)
# 2. Print a summary of all pizzas ordered
# 3. Handle invalid input more gracefully
