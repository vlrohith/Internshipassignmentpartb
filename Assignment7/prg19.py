def remove_duplicates_from_list_of_lists(list_of_lists):
  unique_list_of_lists = set()
  for list1 in list_of_lists:
    unique_list_of_lists.add(tuple(list1))
  return list(unique_list_of_lists)

list_of_lists = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
unique_list_of_lists = remove_duplicates_from_list_of_lists(list_of_lists)

print(unique_list_of_lists)
