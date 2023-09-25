# Original list of strings
original_list = ['red', 'black', 'white', 'green', 'orange']

# Function to filter elements containing a specific substring
find_substring = lambda lst, substring: list(filter(lambda s: substring in s, lst))

# Substring to search for
substring1 = 'ack'
substring2 = 'abc'

# Find elements containing the specific substrings
result1 = find_substring(original_list, substring1)
result2 = find_substring(original_list, substring2)

# Print the results
print("Substring to search:", substring1)
print("Elements of the said list that contain the specific substring:", result1)

print("Substring to search:", substring2)
print("Elements of the said list that contain the specific substring:", result2)
