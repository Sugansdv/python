# banking
from banking import open_account, apply_loan, deposit

print(open_account("Alice"))
print(apply_loan(50000))
print(deposit(3000))

# school
from school.students import register_student
from school.teachers import register_teacher

register_student("John")
register_teacher("Ms. Smith")

# textutils
from textutils import word_count
from textutils.utils import capitalize_text
from textutils.config import DEFAULT_CONFIG

print(word_count("Python is awesome"))
print(capitalize_text("hello world"))
print(DEFAULT_CONFIG)

# shopping_cart
from shopping_cart.cart import add_to_cart
from shopping_cart.items import items
from shopping_cart.checkout import calculate_total

cart = []
add_to_cart(cart, "apple")
add_to_cart(cart, "milk")
print(f"Total: ₹{calculate_total(cart, items)}")

# inventory
from inventory.sales import sell_item
sell_item("banana")
