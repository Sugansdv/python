# main.py

import mymodule
import importlib
import time

print("First call:")
mymodule.greet()

# Simulate external update to the module
print("\n--- Now modify 'mymodule.py' to version 2 and save it. Waiting for 10 seconds... ---")
time.sleep(10)  # Give time to manually edit the module

# Reload the module after manual update
importlib.reload(mymodule)

print("\nAfter reload:")
mymodule.greet()
