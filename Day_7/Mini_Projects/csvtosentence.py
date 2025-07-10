#20. CSV to Sentence Converter

# Input: CSV string from the user
csv_input = input("Enter items (comma-separated): ") 

# Split the input string into a list using .split(',')
items = csv_input.split(',')

# Remove any extra spaces from each item
items = [item.strip() for item in items]

# Generate sentence based on number of items
if len(items) == 0:
    sentence = "You bought nothing."
elif len(items) == 1:
    sentence = f"You bought {items[0]}."
elif len(items) == 2:
    sentence = f"You bought {items[0]} and {items[1]}."
else:
    # Join all but last item with commas, then add ", and last item"
    sentence = f"You bought {', '.join(items[:-1])}, and {items[-1]}."

# Print the final sentence
print(sentence)
