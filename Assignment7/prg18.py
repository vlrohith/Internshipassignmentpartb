def are_all_dicts_empty(list_of_dicts):


  is_all_empty = True
  for dict in list_of_dicts:
    if dict:
      is_all_empty = False
      break
  return is_all_empty

list_of_dicts = [{}, {}, {}]

are_all_dicts_empty = are_all_dicts_empty(list_of_dicts)

print(are_all_dicts_empty)
