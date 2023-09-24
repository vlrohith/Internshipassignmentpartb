def separate_ints_strings_floats(list1):
  """Separates ints, strings, and floats from a list and stores them in separate lists.

  Args:
    list1: A list containing ints, strings, and floats.

  Returns:
    Three lists, one containing ints, one containing strings, and one containing floats.
  """

  int_list = []
  string_list = []
  float_list = []

  for item in list1:
    if isinstance(item, int):
      int_list.append(item)
    elif isinstance(item, str):
      string_list.append(item)
    elif isinstance(item, float):
      float_list.append(item)

  return int_list, string_list, float_list


# Example usage:

list1 = [1, "Jump", 2.3, "Where", 4.5, 6]

int_list, string_list, float_list = separate_ints_strings_floats(list1)

print("Integer list:", int_list)
print("String list:", string_list)
print("Float list:", float_list)
