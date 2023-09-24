def remove_duplicates_from_dict(dict1):

  unique_dict = {}
  for key, value in dict1.items():
    if key not in unique_dict:
      unique_dict[key] = value
  return unique_dict




dict1 = {1: 10, 2: 20, 3: 30, 1: 10, 2: 20}


unique_dict = remove_duplicates_from_dict(dict1)

print(unique_dict)
