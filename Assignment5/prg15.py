def count_repeated_characters(string):
  character_counts = {}
  for character in string:
    if character in character_counts:
      character_counts[character] += 1
    else:
      character_counts[character] = 1
  return character_counts
string = "thequickbrownfoxjumpsoverthelazydog"
character_counts = count_repeated_characters(string)
for character, count in character_counts.items():
  if count > 1:
    print(f"{character}: {count}")