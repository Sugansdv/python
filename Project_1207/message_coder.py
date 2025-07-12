# 22. Message Encoder/Decoder
# Concepts: strings, list, loop, functions.
# • Convert message to ASCII or reverse.
# • Option for encoding/decoding.
# • Use loop to process character-wise.

def encode_message(msg):
    result = []
    for char in msg:
        result.append(str(ord(char)))
    return " ".join(result)

def decode_message(code):
    chars = code.split()
    result = ""
    for c in chars:
        if c.isdigit():
            result += chr(int(c))
    return result

while True:
    print("\n1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        message = input("Enter message to encode: ")
        print("Encoded:", encode_message(message))
    elif choice == "2":
        code = input("Enter ASCII code (space-separated): ")
        print("Decoded:", decode_message(code))
    elif choice == "3":
        break
    else:
        print("Invalid choice.\n")
