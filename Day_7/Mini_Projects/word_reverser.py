# 9. Word Reverser
# Input: sentence from the user
sentence = input("Enter a sentence: ") 

# Split the sentence into words using .split()
words = sentence.split()

# Reverse each word using slicing [::-1]
reversed_words = [word[::-1] for word in words]

# Join the reversed words back into a sentence using .join()
output = " ".join(reversed_words)

print("Reversed sentence:", output)

