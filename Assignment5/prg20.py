def remove_consecutive_duplicates(string):
  result = ""
  previous_character = None
  for character in string:
    if character != previous_character:
      result += character
    previous_character = character
  return result
string = "abcabcbb"
result = remove_consecutive_duplicates(string)
print(result)