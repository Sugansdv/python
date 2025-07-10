# 14. Shape Area Calculator
import math

# • Circle, rectangle, square using individual functions

def area_circle(*args):
    if len(args) == 1:
        r = args[0]
        # • Use lambda for quick formulas
        circle_area = lambda r: math.pi * r * r
        return round(circle_area(r), 2)
    else:
        # • Handle invalid inputs using return conditions
        return "Invalid input for circle. Requires 1 value (radius)."

def area_rectangle(*args):
    if len(args) == 2:
        l, w = args
        rectangle_area = lambda l, w: l * w
        return rectangle_area(l, w)
    else:
        return "Invalid input for rectangle. Requires 2 values (length, width)."

def area_square(*args):
    if len(args) == 1:
        s = args[0]
        square_area = lambda s: s * s
        return square_area(s)
    else:
        return "Invalid input for square. Requires 1 value (side)."

# Menu to choose shape
print("Choose shape to calculate area:")
print("1. Circle\n2. Rectangle\n3. Square")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    radius = float(input("Enter radius: "))
    print("Area of Circle:", area_circle(radius))
elif choice == '2':
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area of Rectangle:", area_rectangle(length, width))
elif choice == '3':
    side = float(input("Enter side: "))
    print("Area of Square:", area_square(side))
else:
    print("Invalid shape choice.")
