def match_key_values(dict1, dict2):

  matched_key_values = []
  for key, value in dict1.items():
    if key in dict2 and dict2[key] == value:
      matched_key_values.append((key, value))
  return matched_key_values


dict1 = {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

matched_key_values = match_key_values(dict1, dict2)

print(matched_key_values)
