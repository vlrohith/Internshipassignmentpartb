def combine_dicts(dict1, dict2):

  combined_dict = {}
  for key, value in dict1.items():
    combined_dict[key] = value
  for key, value in dict2.items():
    if key not in combined_dict:
      combined_dict[key] = value
    else:
      combined_dict[key] += value
  return combined_dict


dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}

combined_dict = combine_dicts(dict1, dict2)

print(combined_dict)
