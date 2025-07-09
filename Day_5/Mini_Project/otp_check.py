#  20. OTP Retry System
# Objective: Simulate OTP entry with retry option.

# • OTP is fixed.
correct_otp = "2468"
attempts = 0

# • Use while loop to allow 3 retries.
while attempts < 3:
    user_otp = input(" Enter OTP: ")

    # • Use break if entered OTP is correct.
    if user_otp == correct_otp:
        print(" OTP verified successfully.")
        break
    else:
        print(" Incorrect OTP. Try again.")
        attempts += 1

# • Use else to print "OTP failed".
else:
    print(" OTP verification failed. Too many attempts.")
