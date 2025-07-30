def word_generator(samples):
    index = 0
    while True:
        yield samples[index % len(samples)]
        index += 1
