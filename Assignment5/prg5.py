def swap_first_two_chars(string):
    first_char = string[0]
    second_char = string[1]
    new_string = second_char + first_char + string[2:]
    return new_string
def combine_strings(string1, string2):
    combined_string = string1 + " " + string2
    return combined_string
string1 = "abc"
string2 = "xyz"
swapped_string1 = swap_first_two_chars(string1)
swapped_string2 = swap_first_two_chars(string2)
combined_string = combine_strings(swapped_string1, swapped_string2)
print(combined_string)