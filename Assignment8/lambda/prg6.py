# Original list of numbers
original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# Use Lambda and filter to find numbers divisible by nineteen or thirteen
divisible_numbers = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, original_list))

# Print the result
print("Numbers of the above list divisible by nineteen or thirteen:", divisible_numbers)
