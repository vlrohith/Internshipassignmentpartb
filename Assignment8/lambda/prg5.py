# Input string
input_string = "12345"

# Check if the string is a number using Lambda
is_number = lambda string: string.isdigit()

# Use the lambda function to check
result = is_number(input_string)

# Print the result
if result:
    print(f"The string '{input_string}' is a number.")
else:
    print(f"The string '{input_string}' is not a number.")
