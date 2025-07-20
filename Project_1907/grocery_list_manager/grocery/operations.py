def add_item(items_by_category, item, category):
    item_entry = (item, category)
    if category not in items_by_category:
        items_by_category[category] = []
    items_by_category[category].append(item_entry)
    print(f" '{item}' added to category '{category}'.")

def remove_item(items_by_category, item):
    found = False
    for category, items in items_by_category.items():
        for i in items:
            if i[0] == item:
                items.remove(i)
                found = True
                print(f"'{item}' removed from category '{category}'.")
                break
    if not found:
        print(" Item not found.")

def mark_bought(items_by_category, bought_items, item):
    for category, items in items_by_category.items():
        for i in items:
            if i[0] == item:
                bought_items.add(item)
                print(f" '{item}' marked as bought.")
                return
    print(" Item not found.")

def display_by_category(items_by_category, bought_items):
    if not items_by_category:
        print("📭 No items in the grocery list.")
        return
    for category in sorted(items_by_category):
        print(f"\n Category: {category}")
        for item, _ in items_by_category[category]:
            status = "✔️" if item in bought_items else "❌"
            print(f"  {status} {item}")

def search_items(items_by_category, keyword):
    keyword = keyword.lower()
    found = False
    print("\n Search Results:")
    for category, items in items_by_category.items():
        for item, _ in items:
            if keyword in item.lower():
                print(f" {item} (Category: {category})")
                found = True
    if not found:
        print(" No matching items found.")
