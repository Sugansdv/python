# ==== MINI PROJECT 18: PRIME NUMBER FINDER (1–50) ====

print("====================")
print("Prime Number Finder (1–50)")
print("====================")

# Loop through numbers from 2 to 50
for num in range(2, 51):
    # Use a flag variable to check divisibility
    is_prime = True
    
    # Use nested loops to check for divisors
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break  # Not a prime, exit inner loop
    
    # If no divisor found → prime
    if is_prime:
        print(num, end=" ")
