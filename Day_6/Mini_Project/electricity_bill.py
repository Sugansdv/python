# 6. Electricity Bill Calculator

# • Take monthly units as arguments
def calculate_bill(*units):
    total = 0
    for u in units:
        # • Calculate and return the bill using slabs
        if u <= 100:
            total += u * 2
        elif u <= 200:
            total += (100 * 2) + (u - 100) * 5
        else:
            total += (100 * 2) + (100 * 5) + (u - 200) * 10
    return total

# • Add GST using lambda
add_gst = lambda amount: round(amount * 1.18, 2)

bill = calculate_bill(120, 80, 150)
print("Total without GST: ₹", bill)
print("Total with GST: ₹", add_gst(bill))
