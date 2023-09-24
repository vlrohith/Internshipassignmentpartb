def print_index_of_character(string, character):
  index = string.find(character)
  if index != -1:
    print(f"The index of the character '{character}' in the string '{string}' is {index}.")
  else:
    print(f"The character '{character}' is not found in the string '{string}'.")
string = "Hello, world!"
character = "o"
print_index_of_character(string, character)
string = "Python"
character = "z"
print_index_of_character(string, character)