def sum_dict_items(dict1):

  sum = 0
  for value in dict1.values():
    sum += value
  return sum

dict1 = {1: 10, 2: 20, 3: 30}

sum = sum_dict_items(dict1)

print(sum)
