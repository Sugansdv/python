# 8. Language Translator
# Description: English to Tamil dictionary.
# Requirements:
# - Structure: {english_word: tamil_word}
# - Allow adding, updating, and deleting translations
# - Search and return Tamil word using .get()
# - Reverse translation using swapped dictionary
# - Use in to check availability

translator = {
    "hello": "வணக்கம்",
    "water": "தண்ணீர்",
    "book": "நூல்",
    "food": "உணவு"
}

def add_or_update_word(english, tamil):
    translator[english.lower()] = tamil
    print(f"'{english}' added/updated.")

def delete_word(english):
    if english in translator:
        del translator[english]
        print(f"'{english}' deleted.")
    else:
        print(f"'{english}' not found.")

def translate_to_tamil(english):
    tamil = translator.get(english.lower())
    if tamil:
        print(f"{english} → {tamil}")
    else:
        print("Translation not found.")

def reverse_translate(tamil_word):
    reversed_dict = {v: k for k, v in translator.items()}
    if tamil_word in reversed_dict:
        print(f"{tamil_word} → {reversed_dict[tamil_word]}")
    else:
        print("Reverse translation not found.")

add_or_update_word("School", "பள்ளி")
translate_to_tamil("Food")
translate_to_tamil("School")
delete_word("Water")
reverse_translate("நூல்")
reverse_translate("நன்றி")
