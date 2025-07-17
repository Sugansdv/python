# 10. Recipe Ingredient Matcher
# Goal: Match ingredients available at home with a recipe.
# Requirements:
# - Create a set of available ingredients.
# - Compare with required ingredients using issuperset().
# - Suggest missing items using difference().
# Concepts Covered: issuperset(), difference(), in.

available = {"eggs", "flour", "milk", "sugar", "butter"}
required = {"flour", "milk", "sugar", "vanilla"}

can_make_recipe = available.issuperset(required)
missing = required.difference(available)

print("Can make recipe:", can_make_recipe)
print("Missing ingredients:", missing)
