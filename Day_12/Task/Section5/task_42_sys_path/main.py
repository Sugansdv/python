import sys
import os

# Show sys.path before
print("Before:", sys.path)

# Add custom folder to sys.path
extra_path = os.path.join(os.getcwd(), 'extra')
sys.path.append(extra_path)

# Show sys.path after
print("After:", sys.path)

# Import the module from extra/
import mymodule
mymodule.greet()
