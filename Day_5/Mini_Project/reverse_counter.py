# 13. Reverse Counter App
# Objective: Count down from any number to 1.

# • Input: starting number
try:
    num = int(input("Enter a starting number: "))
except ValueError:
    print(" Invalid input. Please enter a number.")
else:
    # • Use while loop to count down.
    while num > 0:
        print(num)
        num -= 1

        # • Stop if number becomes zero using break.
        if num == 0:
            print(" Countdown finished!")
            break
