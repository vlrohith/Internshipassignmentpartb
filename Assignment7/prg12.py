def get_max_and_min_dict_values(dict1):


  max_value = max(dict1.values())
  min_value = min(dict1.values())
  return max_value, min_value


dict1 = {1: 10, 2: 20, 3: 30}


max_value, min_value = get_max_and_min_dict_values(dict1)

print("Maximum value:", max_value)
print("Minimum value:", min_value)
