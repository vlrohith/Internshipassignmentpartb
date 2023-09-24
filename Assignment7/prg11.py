def sort_dict_by_key(dict1):


  sorted_dict = sorted(dict1.items(), key=lambda item: item[0])
  return sorted_dict

dict1 = {1: 10, 2: 20, 3: 30}


sorted_dict = sort_dict_by_key(dict1)

print(sorted_dict)
