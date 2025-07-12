#  17. Daily Meal Planner
# Description: Store meal plans for a week.

# Use a nested list: [[“Monday”, “Idly”], …]
meal_plan = [
    ["Monday", "Idly"],
    ["Tuesday", "Chapati"],
    ["Wednesday", "Pasta"],
    ["Thursday", "Dosa"],
    ["Friday", "Rice & Curry"],
    ["Saturday", "Pizza"],
    ["Sunday", "Biriyani"]
]

# Display full weekly meal plan
print(" Weekly Meal Plan:")
for day, meal in meal_plan:
    print(f"{day}: {meal}")

# Update meals (change Wednesday's meal to "Paratha")
for plan in meal_plan:
    if plan[0] == "Wednesday":
        plan[1] = "Paratha"
        print("\nUpdated Wednesday's meal to 'Paratha'")

# Remove a meal (remove Thursday)
for plan in meal_plan:
    if plan[0] == "Thursday":
        meal_plan.remove(plan)
        print("Removed Thursday from meal plan")
        break

# Slice to view weekend plans (Saturday & Sunday)
weekend_plan = meal_plan[-2:]  # Last 2 items
print("\n Weekend Meal Plan:")
for day, meal in weekend_plan:
    print(f"{day}: {meal}")

# Final display
print("\n Final Weekly Meal Plan:")
for day, meal in meal_plan:
    print(f"{day}: {meal}")
