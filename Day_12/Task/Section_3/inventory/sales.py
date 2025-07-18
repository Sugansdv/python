from .stock import update_stock  # relative import

def sell_item(item):
    update_stock(item, -1)
    print(f"{item} sold")
