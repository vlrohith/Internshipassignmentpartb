# Original mixed list of integers and strings
original_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# Separate numbers and strings
numbers = [x for x in original_list if isinstance(x, int)]
strings = [x for x in original_list if isinstance(x, str)]

# Sort numbers and strings
sorted_numbers = sorted(numbers)
sorted_strings = sorted(strings)

# Combine sorted numbers and strings
sorted_mixed_list = sorted_numbers + sorted_strings

# Print the sorted mixed list
print("Sort the said mixed list of integers and strings:", sorted_mixed_list)
