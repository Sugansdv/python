#14. Text Highlighter
 # Input: paragraph and keyword from the user
paragraph = input("Enter a paragraph: ")    
keyword = input("Enter the keyword to highlight: ")

# Count how many times the keyword appears 
count = paragraph.lower().count(keyword.lower())

# Replace all occurrences with uppercase keyword 
words = paragraph.split()
highlighted = " ".join([word.upper() if word.lower() == keyword.lower() else word for word in words])

# Print the highlighted paragraph and count
print("\nHighlighted Paragraph:\n", highlighted)
print("\nOccurrences of keyword:", count)
