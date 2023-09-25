# Input string and character
input_string = "Hello, world!"
start_character = "H"

# Check if the string starts with the character using Lambda
starts_with_character = lambda string, char: string.startswith(char)

# Use the lambda function to check
result = starts_with_character(input_string, start_character)

# Print the result
if result:
    print(f"The string '{input_string}' starts with the character '{start_character}'.")
else:
    print(f"The string '{input_string}' does not start with the character '{start_character}'.")
