def convert_to_uppercase_if_contains_uppercase_characters(string):
    uppercase_character_count = 0
    for i in range(4):
        if string[i].isupper():
            uppercase_character_count += 1
    if uppercase_character_count >= 2:
        return string.upper()
    else:
        return string
string = "Hello, world!"
converted_string = convert_to_uppercase_if_contains_uppercase_characters(
    string)
print(converted_string)

string = "PYthon"
converted_string = convert_to_uppercase_if_contains_uppercase_characters(
    string)
print(converted_string)