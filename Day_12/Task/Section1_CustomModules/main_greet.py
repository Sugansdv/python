#Task 10
import greetings_util

def welcome_users():
    users = ["Alice", "Bob", "Charlie"]
    for user in users:
        greetings_util.greet(user)

if __name__ == "__main__":
    welcome_users()
