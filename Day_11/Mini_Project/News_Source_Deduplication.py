
# 11. News Source Deduplication
# Goal: Identify and remove duplicate headlines.
# Requirements:
# - Convert fetched headlines from multiple APIs to sets.
# - Compare duplicates using intersection().
# - Store unique headlines using union().
# Concepts Covered: intersection(), union(), membership.

api1 = {"Stocks up today", "Weather alert", "Tech merger announced"}
api2 = {"Weather alert", "Election results", "Tech merger announced"}

duplicates = api1.intersection(api2)
all_unique = api1.union(api2)

print("Duplicate headlines:", duplicates)
print("All unique headlines:", all_unique)
