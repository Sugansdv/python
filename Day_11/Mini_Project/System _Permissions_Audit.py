# 19. System Permissions Audit
# Goal: Check if users have all required access.
# Requirements:
# - Store required permissions in a set.
# - Use issubset() to validate user permission sets.
# - Output missing permissions with difference().
# Concepts Covered: issubset(), difference().

required_permissions = {"read", "write", "execute"}

user_permissions = {
    "alice": {"read", "write", "execute"},
    "bob": {"read", "write"},
    "charlie": {"read", "execute"},
}

for user, perms in user_permissions.items():
    if required_permissions.issubset(perms):
        print(f"{user} has all required permissions.")
    else:
        missing = required_permissions.difference(perms)
        print(f"{user} is missing: {missing}")
