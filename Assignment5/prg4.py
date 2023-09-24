def replace_first_char(string):
    first_char = string[0]
    new_string = first_char
    for char in string[1:]:
        if char == first_char:
            new_string += '$'
        else:
            new_string += char
    return new_string
string = "restart"
result = replace_first_char(string)
print(result)