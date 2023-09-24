def sort_dict_by_value(dict1, ascending=True):
  
  sorted_list = sorted(dict1.items(), key=lambda item: item[1], reverse=not ascending)
  return sorted_list

dict1 = {"a": 1, "b": 2, "c": 3}

sorted_list_ascending = sort_dict_by_value(dict1)

sorted_list_descending = sort_dict_by_value(dict1, ascending=False)

print("Sorted list in ascending order:", sorted_list_ascending)
print("Sorted list in descending order:", sorted_list_descending)
