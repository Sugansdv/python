
from cart_utils.cart import add_to_cart, remove_from_cart, display_cart

# Initialize shopping cart (Dictionary with tuple keys)
cart = {}

# Add items
add_to_cart(cart, ("P001",), "Wireless Mouse", 799, "Electronics")
add_to_cart(cart, ("P002",), "Cotton T-Shirt", 499, "Clothing")
add_to_cart(cart, ("P001",), "Wireless Mouse", 799, "Electronics")  # Duplicate item ID
add_to_cart(cart, ("P003",), "LED Lamp", 299, "Home")

# Display
display_cart(cart)

# Remove one item
remove_from_cart(cart, ("P002",))

# Display again
display_cart(cart)
