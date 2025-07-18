# Dictionary to hold signal status
signals = {}

# Set to hold currently active lights
active_lights = set()

def set_signal(location, time, status):
    key = (location, time)  # Tuple as unique identifier
    signals[key] = status
    active_lights.add(status)

def get_signal(location, time):
    return signals.get((location, time), "No signal found")

def is_valid_signal(status):
    return status in {"RED", "YELLOW", "GREEN"}
