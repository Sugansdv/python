def send_message(users, chat_logs):
    sender = input("Sender username: ").strip()
    receiver = input("Receiver username: ").strip()
    
    if sender not in users or receiver not in users:
        print("Both users must be registered.")
        return

    message = input("Enter message: ").strip()
    key = tuple(sorted((sender, receiver)))
    chat_logs.setdefault(key, []).append(f"{sender}: {message}")
    print("Message sent.")

def view_messages(users, chat_logs):
    user1 = input("Enter first username: ").strip()
    user2 = input("Enter second username: ").strip()

    if user1 not in users or user2 not in users:
        print("Users not found.")
        return

    key = tuple(sorted((user1, user2)))
    if key not in chat_logs or not chat_logs[key]:
        print("No messages found.")
        return

    print(f"Chat history between {user1} and {user2}:")
    for msg in chat_logs[key]:
        print(f"  {msg}")

def delete_messages(users, chat_logs):
    user1 = input("Enter first username: ").strip()
    user2 = input("Enter second username: ").strip()

    if user1 not in users or user2 not in users:
        print("Users not found.")
        return

    key = tuple(sorted((user1, user2)))
    if key in chat_logs:
        chat_logs[key].clear()
        print("Chat history deleted.")
    else:
        print("No chat history to delete.")
