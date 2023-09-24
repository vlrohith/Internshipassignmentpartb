def generate_dict(n):


  dict1 = {}
  for i in range(1, n + 1):
    dict1[i] = i * i
  return dict1

n = 5
dict1 = generate_dict(n)

print(dict1)
