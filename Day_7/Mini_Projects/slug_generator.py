#16. Slug Generator for Blog Titles
# Input: blog title from the user
title = input("Enter your blog title: ")  # Example:  Python   Basics for Beginners 

# Remove leading/trailing spaces using .strip()
title = title.strip()

# Replace multiple spaces with single space.
# This step ensures clean conversion before replacing with dashes
title = " ".join(title.split())

# Convert to lowercase using .lower()
title = title.lower()

# Replace all spaces with hyphens using .replace()
slug = title.replace(" ", "-")

# Print the final slug
print("Generated Slug:", slug)

