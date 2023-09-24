def reverse_string_if_multiple_of_4(input_string):
    if len(input_string) % 4 == 0:
        reversed_string = ''.join(reversed(input_string))
        return reversed_string
    else:
        return input_string
input_str1 = "Hello"
result1 = reverse_string_if_multiple_of_4(input_str1)
print(result1)
input_str2 = "Jumphere"
result2 = reverse_string_if_multiple_of_4(input_str2)
print(result2)  