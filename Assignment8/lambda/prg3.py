# Original list of dictionaries
original_list = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sorting the list of dictionaries using Lambda
sorted_list = sorted(original_list, key=lambda x: x['make'])

# Print the sorted list
print("Sorting the List of dictionaries:", sorted_list)
