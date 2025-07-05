# ==== MINI PROJECT 15: LIST SEARCH WITH BREAK ====

print("====================")
print("List Search with Break")
print("====================")

# Sample product list
products = ["Rice", "Milk", "Sugar", "Oil", "Salt"]

# Input: product to search
search_item = input("Enter the product to search: ").strip().title()

# Use for loop to search
for product in products:
    # If found, print “Product Found” and break
    if product == search_item:
        print("Product Found!")
        break
# If not found after loop, use else to print “Not Found”
else:
    print("Product Not Found.")
