def unique_words(words):
    unique_words = set(words)
    unique_words = sorted(unique_words)
    return unique_words
words = "red, white, black, red, green, black".split(",")
unique_words = unique_words(words)
print(unique_words)