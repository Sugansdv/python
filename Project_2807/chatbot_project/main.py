from core.bot import Chatbot

def main():
    bot = Chatbot("core/responses.json")
    print(" Chatbot is ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Bot: Goodbye!")
            break
        response = bot.get_response(user_input)
        print("Bot:", response)

    print("\nBot Rules (from generator):")
    for rule in bot.response_generator():
        print("-", rule)

if __name__ == "__main__":
    main()
