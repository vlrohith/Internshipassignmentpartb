def swap_comma_and_dot(string):
  translation_table = str.maketrans(".", ",", ",")
  swapped_string = string.translate(translation_table)
  return swapped_string
string = "32.054,23"
swapped_string = swap_comma_and_dot(string)
print(swapped_string)