def multiply_dict_items(dict1):
 

  product = 1
  for value in dict1.values():
    product *= value
  return product



dict1 = {1: 10, 2: 20, 3: 30}

product = multiply_dict_items(dict1)

print(product)
