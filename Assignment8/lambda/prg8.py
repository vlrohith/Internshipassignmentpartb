# Input string
input_string = "PaceWisd0m"

# Check if the string is valid using Lambda
is_valid_string = lambda s: any(c.isupper() for c in s) and any(c.islower() for c in s) \
                          and any(c.isdigit() for c in s) and len(s) >= 10

# Use the lambda function to check
result = is_valid_string(input_string)

# Print the result
if result:
    print(f"The string '{input_string}' is a valid string.")
else:
    print(f"The string '{input_string}' is not a valid string.")
