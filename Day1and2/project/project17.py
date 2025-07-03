## 17. Unique Visitor Counter
print("========================================")
print("          Unique Visitor Counter        ")
print("========================================")

# 1. Ask for names of people entering the shop (5 times)
visitors = set()

for i in range(1, 6):
    name = input(f"Enter name of visitor {i}: ")
    visitors.add(name)  # Set automatically removes duplicates

# 2. Print all unique visitor names
print("\n Unique Visitors:")
print(visitors)

# 3. Print the number of unique visitors
print(f"\n Total Unique Visitors: {len(visitors)}")
