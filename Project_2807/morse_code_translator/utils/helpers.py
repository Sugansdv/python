def morse_generator(text, translator):
    morse_code = translator.to_morse(text)
    for symbol in morse_code.split():
        yield symbol