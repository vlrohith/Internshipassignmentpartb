def count_characters(string):
  character_counts = {}
  for character in string:
    if character in character_counts:
      character_counts[character] += 1
    else:
      character_counts[character] = 1
  return character_counts
string = "google.com'"
character_counts = count_characters(string)
print(character_counts)