from timer.core import PomodoroTimer
from utils.helpers import notify, time_generator

def main():
    print("Welcome to the Pomodoro Timer!")

    try:
        work = int(input("Enter work session duration (in minutes): "))
        short_break = int(input("Enter short break duration (in minutes): "))
        long_break = int(input("Enter long break duration (in minutes): "))
        sessions = int(input("Enter number of pomodoro sessions: "))
    except ValueError:
        print("Please enter valid integer values.")
        return

    timer = PomodoroTimer(work, short_break, long_break, sessions)
    timer.start()

if __name__ == "__main__":
    main()
