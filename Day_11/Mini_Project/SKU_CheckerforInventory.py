# 13. Duplicate SKU Checker for Inventory
# Goal: Identify duplicate product SKUs in stock.
# Requirements:
# - Convert SKU list to a set.
# - Compare lengths of original list and set to detect duplicates.
# - Store duplicates separately.
# Concepts Covered: Set creation, len(), membership.

sku_list = ["A123", "B456", "A123", "C789", "B456", "D001"]
unique_skus = set(sku_list)
has_duplicates = len(sku_list) != len(unique_skus)
duplicates = {sku for sku in sku_list if sku_list.count(sku) > 1}

print("Contains duplicates:", has_duplicates)
print("Duplicate SKUs:", duplicates)
print("Unique SKUs in inventory:", unique_skus)
