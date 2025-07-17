# 16. FrozenSet for Immutable Data
# Goal: Store fixed data in a dictionary.
# Requirements:
# - Use frozenset as dictionary keys.
# - Store meal combinations as frozen sets.
# - Retrieve data using set lookup.
# Concepts Covered: frozenset, immutability, dictionary integration.

meal_combinations = {
    frozenset(["rice", "chicken", "salad"]): "High Protein",
    frozenset(["pasta", "tomato", "basil"]): "Italian Classic",
    frozenset(["bread", "cheese", "ham"]): "Quick Snack"
}

search_combo = frozenset(["chicken", "salad", "rice"])
meal_type = meal_combinations.get(search_combo, "Unknown Meal")

print("Meal type for given combo:", meal_type)
