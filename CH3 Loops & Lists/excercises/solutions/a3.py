# Answer 3: Shopping Cart with While Loop

cart = []

while True:
    item = input("Enter item (or 'done' to finish): ")
    
    if item == "done":
        break
    elif item == "remove":
        to_remove = input("What to remove? ")
        if to_remove in cart:
            cart.remove(to_remove)
        else:
            print(f"{to_remove} not in cart.")
    else:
        cart.append(item)

print(f"Final cart: {cart}")
print(f"Total items: {len(cart)}")