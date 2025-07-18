def greet():
    print("Hello from helper!")

print("helper.py: __name__ =", __name__)

if __name__ == "__main__":
    print("Running helper.py directly")
    greet()
