# 7. Multi-line Quote Saver
# Accept multi-line quote using triple quotes
quote = input("Paste your multi-line quote:\n""" + "\n") 

# Strip leading/trailing spaces using .strip()
cleaned_quote = quote.strip()

# Count number of lines using .count('\n') + 1
line_count = cleaned_quote.count('\n') + 1

print("\nSaved Quote:\n" + cleaned_quote)
print(f"\nTotal Lines: {line_count}")
