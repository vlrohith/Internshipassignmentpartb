def find_smallest_and_largest_word(string):
  words = string.split()
  smallest_word = min(words, key=len)
  largest_word = max(words, key=len)
  return smallest_word, largest_word
string = "This is a sample string."
smallest_word, largest_word = find_smallest_and_largest_word(string)
print(f"The smallest word in the string is '{smallest_word}'.")
print(f"The largest word in the string is '{largest_word}'.")