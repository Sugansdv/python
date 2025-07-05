# Restaurant Bill Splitter

# Ask how many food items
num_items = int(input("How many food items? "))

# Input: prices of food items (one by one)
food_prices = []
for i in range(num_items):
    price = float(input(f"Enter price of item {i+1}: ₹"))
    food_prices.append(price)

# Use loop to calculate total
total_bill = 0
for price in food_prices:
    total_bill += price

# Input number of friends → split amount using division
num_friends = int(input("Enter number of friends to split the bill: "))

# Prevent division by zero
if num_friends <= 0:
    print("Number of friends must be at least 1.")
else:
    split_amount = total_bill / num_friends

    # Print the result
    print("\n========= Bill Split Summary =========")
    print(f"Food Item Prices : {food_prices}")
    print(f"Total Bill       : ₹{total_bill:.2f}")
    print(f"Number of Friends: {num_friends}")
    print(f"Each Pays        : ₹{split_amount:.2f}")
    print("======================================")
