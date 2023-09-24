def concatenate_dicts(dicts):

  new_dict = {}
  for dict in dicts:
    new_dict.update(dict)
  return new_dict

dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

new_dict = concatenate_dicts([dict1, dict2, dict3])

print(new_dict)
