# 14. Social Media Post Scheduler
# Description: Schedule and manage posts.

# Store post titles in a list
post_queue = [
    "New Product Launch ",
    "Monday Motivation ",
    "User Testimonials "
]

# Display current post queue
print(" Scheduled Posts:")
for i, post in enumerate(post_queue, start=1):
    print(f"{i}. {post}")

# Insert priority post using insert()
priority_post = "Breaking News "
post_queue.insert(0, priority_post)
print(f"\n Inserted priority post: '{priority_post}' at the top")

# Remove posted item with pop()
posted = post_queue.pop(0)
print(f"\n Posted and removed: '{posted}'")

# Display remaining queue
print("\n Remaining Scheduled Posts:")
for i, post in enumerate(post_queue, start=1):
    print(f"{i}. {post}")
