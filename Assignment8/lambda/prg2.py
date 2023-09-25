# Original list of tuples
original_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Sorting the list of tuples using Lambda
sorted_list = sorted(original_list, key=lambda x: x[1])  # Sort based on the second element of each tuple

# Print the sorted list
print("Sorting the List of Tuples:", sorted_list)
