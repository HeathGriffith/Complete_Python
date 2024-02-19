# Ternary operations
# Sytnax: variable = value_if_true if condition else value_if_false

# Example 1: operation assigns a value to 'can_message' based on the truthiness of 'is_friend'

# Condition setup: Whether someone is considered a friend
is_friend = False

# Ternary operation: Assigns "message allowed" to 'can_message' if 'is_friend' is True, otherwise assigns "not allowed to message."
can_message = "message allowed" if is_friend else "not allowed to message."

# Result based on the current value of 'is_friend'
print(can_message)  # Output: "not allowed to message."


# Example 2: Assigning a Discount Based on Purchase Amount

# Example purchase amount
purchase_amount = 120

# Apply a 10% discount for purchases over $100, otherwise apply a 5% discount
discount = 0.1 if purchase_amount > 100 else 0.05

# Calculate final price
final_price = purchase_amount * (1 - discount)

# Output the result
print(f"Original price: ${purchase_amount}")
print(f"Discount applied: {discount * 100}%")
print(f"Final price: ${final_price:.2f}")
