from traffic_control import set_signal, get_signal, is_valid_signal, active_lights

# Set signals
set_signal("Junction-A", "08:00", "RED")
set_signal("Junction-B", "08:00", "GREEN")
set_signal("Junction-C", "08:00", "YELLOW")

# Get signal status
print(get_signal("Junction-B", "08:00"))  # GREEN

# Check if a signal is valid
print(is_valid_signal("BLUE"))  # False

# Show all active lights
print("Active lights:", active_lights)
