# 6. Email Categorization Tool
# Goal: Assign unique tags to emails.
# Requirements:
# - Extract unique hashtags or topics from content.
# - Use set comprehension to collect tags.
# - Use join() to display tags as a single string.
# Concepts Covered: Set comprehension, uniqueness, iteration.

email_content = """
Welcome to our newsletter! #updates #news
Learn more about our #products and #offers.
Stay tuned for #news and upcoming #events.
"""

tags = {word for word in email_content.split() if word.startswith("#")}
tag_string = ", ".join(tags)

print("Extracted Tags:", tag_string)
