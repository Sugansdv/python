# 25. Simple Chatbot (Menu-Based)
# Concepts: string comparison, functions, loop.
# • Handle inputs like "Hi", "What is your name?", etc.
# • Respond using if-else or dictionary map.
# • Exit on "bye".

def get_response(message):
    msg = message.lower()
    if msg in ["hi", "hello"]:
        return "Hello! How can I help you?"
    elif msg == "what is your name?":
        return "I'm a simple chatbot."
    elif msg == "how are you?":
        return "I'm doing fine, thank you!"
    elif msg == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

while True:
    user_input = input("You: ")
    response = get_response(user_input)
    print("Bot:", response)
    if user_input.lower() == "bye":
        break
