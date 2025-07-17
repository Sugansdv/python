# 5. Access Control List Manager
# Goal: Manage user access rights using sets.
# Requirements:
# - Maintain sets for admin, editor, and viewer roles.
# - Use issubset() to check if editor ⊆ admin.
# - Use issuperset() for admin access check.
# - Use isdisjoint() to prevent conflicting roles.
# Concepts Covered: issubset(), issuperset(), isdisjoint().

admin_users = {"alice", "bob", "carol"}
editor_users = {"bob", "carol"}
viewer_users = {"dave", "eve"}

is_editor_subset_admin = editor_users.issubset(admin_users)
has_admin_access = admin_users.issuperset({"bob"})
conflict = admin_users.isdisjoint(viewer_users)

print("Is editor subset of admin?", is_editor_subset_admin)
print("Does admin have 'bob'?", has_admin_access)
print("Are admin and viewer roles disjoint?", conflict)
