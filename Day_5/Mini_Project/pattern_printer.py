# 12. Pattern Printer
# Objective: Print a star pattern using while.

rows = 5
i = 1

# • Use nested while loop.
while i <= rows:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1

    # • Use pass for lines you want to skip in future.
    pass  

    print() 
    i += 1
