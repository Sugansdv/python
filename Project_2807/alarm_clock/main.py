from alarm.alarm import set_alarm

def main():
    try:
        alarm_time = input("Set alarm time (HH:MM in 24-hour format): ")
        set_alarm(alarm_time)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
