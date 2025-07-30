import time
import os
import pygame

def notify(title, message):
    print(f"\n {title}: {message}")
    try:
        pygame.mixer.init()
        beep_path = os.path.join(os.path.dirname(__file__), "beep.wav")
        if os.path.exists(beep_path):
            pygame.mixer.music.load(beep_path)
            pygame.mixer.music.play()
            time.sleep(2)
    except Exception as e:
        print("Notification sound failed:", e)

def time_generator(seconds):
    while seconds:
        yield seconds
        seconds -= 1

def save_session(text):
    os.makedirs("data", exist_ok=True)
    with open("data/sessions.txt", "a") as f:
        f.write(text + "\n")
