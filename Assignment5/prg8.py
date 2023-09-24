def longest_word_length(words):
    longest_word_length = 0
    for word in words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)
    return longest_word_length
words = ["hello", "world", "Jumpwhere", "Hi", "long"]
longest_word_length = longest_word_length(words)
print(longest_word_length)