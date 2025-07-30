import time
from utils.helpers import notify, time_generator, save_session

class PomodoroTimer:
    def __init__(self, work, short_break, long_break, sessions):
        self.work = work
        self.short_break = short_break
        self.long_break = long_break
        self.sessions = sessions

    def start(self):
        for i in range(1, self.sessions + 1):
            print(f"\n Session {i}: Work for {self.work} minutes")
            self._run_timer(self.work * 60)

            save_session(f"Work session {i} complete")

            if i % 4 == 0:
                print(f" Long Break: {self.long_break} minutes")
                self._run_timer(self.long_break * 60)
            elif i != self.sessions:
                print(f" Short Break: {self.short_break} minutes")
                self._run_timer(self.short_break * 60)

        print("\n All Pomodoro sessions complete!")
        notify("Pomodoro", "All sessions complete! Great job!")

    def _run_timer(self, duration):
        for remaining in time_generator(duration):
            mins, secs = divmod(remaining, 60)
            print(f"  {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
        notify("Pomodoro", "Time's up!")
