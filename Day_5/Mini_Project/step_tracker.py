#  17. Step Tracker
# Objective: Track steps walked daily.

total_steps = 0
day = 1
valid_days = 0

# • Input steps daily for 7 days.
while day <= 7:
    try:
        steps = int(input(f" Enter steps for Day {day}: "))

        # • If any entry is 0, skip with continue.
        if steps == 0:
            print(" Skipping Day (0 steps entered).")
            day += 1
            continue

        total_steps += steps
        valid_days += 1
        day += 1

    except ValueError:
        print(" Please enter a valid number.")

# • After 7 entries, print total and average using else.
else:
    print("\n Step Summary:")
    print(f" Total Steps: {total_steps}")
    if valid_days > 0:
        average = total_steps / valid_days
        print(f" Average (on {valid_days} valid days): {average:.2f}")
    else:
        print("No valid step entries recorded.")
