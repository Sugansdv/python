from abc import ABC, abstractmethod

# Base Class
class Device(ABC):
    def __init__(self, name):
        self.name = name
        self.status = False  # False = Off, True = On

    @abstractmethod
    def operate(self, action):
        pass

    def __str__(self):
        return f"{self.name} is {'ON' if self.status else 'OFF'}"

# Light Device
class Light(Device):
    def operate(self, action):
        if action == "on":
            self.status = True
        elif action == "off":
            self.status = False
        print(f"Light '{self.name}' turned {'ON' if self.status else 'OFF'}")

# Fan Device
class Fan(Device):
    def operate(self, action):
        if action == "on":
            self.status = True
        elif action == "off":
            self.status = False
        print(f"Fan '{self.name}' turned {'ON' if self.status else 'OFF'}")

# AC Device
class AC(Device):
    def operate(self, action):
        if action == "on":
            self.status = True
        elif action == "off":
            self.status = False
        print(f"AC '{self.name}' turned {'ON' if self.status else 'OFF'}")

# SmartHub composed with devices
class SmartHub:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)
        print(f"Added device: {device.name}")

    def control_device(self, name, action):
        for device in self.devices:
            if device.name.lower() == name.lower():
                device.operate(action)
                return
        print(f"No device found with name '{name}'")

    def show_status(self):
        for device in self.devices:
            print(device)

# --- Sample Usage ---
if __name__ == "__main__":
    hub = SmartHub()
    
    # Add devices
    hub.add_device(Light("Bedroom Light"))
    hub.add_device(Fan("Ceiling Fan"))
    hub.add_device(AC("Living Room AC"))
    
    # Control devices
    hub.control_device("Bedroom Light", "on")
    hub.control_device("Ceiling Fan", "on")
    hub.control_device("Living Room AC", "off")
    
    print("\nDevice Statuses:")
    hub.show_status()
