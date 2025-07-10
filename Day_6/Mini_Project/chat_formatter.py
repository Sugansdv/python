#17. Chat Formatter
from datetime import datetime

# • Function accepts multiple messages
def format_chat(*messages):
    # • Use map() with lambda for formatting
    formatted = map(lambda msg: f"[{datetime.now().strftime('%H:%M')}] {msg.capitalize()}", messages)
    
    # • Return messages capitalized, with timestamps (hardcoded or generated)
    return list(formatted)

# Sample usage
chat = format_chat("hello", "how are you?", "i'm good", "bye")
for line in chat:
    print(line)
