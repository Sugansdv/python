# 7. Library Book Management
# Goal: Maintain a catalog of books across multiple branches.
# Requirements:
# - Store each branch’s book list as a set.
# - Use union() to find all available books.
# - Use intersection() to find common books.
# - Use difference() to find books only in one branch.
# Concepts Covered: All set operations.

branch_a = {"1984", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick"}
branch_b = {"Moby Dick", "War and Peace", "1984", "Hamlet"}

all_books = branch_a.union(branch_b)
common_books = branch_a.intersection(branch_b)
unique_to_a = branch_a.difference(branch_b)

print("All books available:", all_books)
print("Books in both branches:", common_books)
print("Books only in Branch A:", unique_to_a)
