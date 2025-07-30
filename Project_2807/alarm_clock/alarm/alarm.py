import datetime
import time
from playsound import playsound
from utils.decorators import snooze

def validate_time_format(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False

@snooze()
def play_alarm_sound():
    print(" Wake up! Alarm ringing!")
    playsound("sound/alarm.mp3")

def set_alarm(alarm_time):
    if not validate_time_format(alarm_time):
        raise ValueError("Invalid time format. Please use HH:MM (24-hour format).")

    print(f"Alarm set for {alarm_time}...")

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            play_alarm_sound()
            break
        time.sleep(30)  # Reduce CPU usage
