def get_highest_3_values(dict1):

  dict_list = list(dict1.items())

  dict_list.sort(key=lambda item: item[1], reverse=True)

  highest_3_values = dict_list[:3]

  highest_3_values_dict = dict(highest_3_values)

  return highest_3_values_dict

dict1 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}

highest_3_values_dict = get_highest_3_values(dict1)

print(highest_3_values_dict)
