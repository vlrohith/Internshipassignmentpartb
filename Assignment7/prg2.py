def add_key_to_dict(dict1, key, value):


  dict1[key] = value
  return dict1

dict1 = {0: 10, 1: 20}

dict1 = add_key_to_dict(dict1, 2, 30)

print(dict1)
