def unit_converter(weight, height, unit):
    if unit == "kg/cm":
        return weight, height
    elif unit == "lb/ft":
        weight_kg = weight * 0.453592
        height_cm = height * 30.48
        return weight_kg, height_cm
    else:
        raise ValueError("Unsupported unit. Use 'kg/cm' or 'lb/ft'.")

