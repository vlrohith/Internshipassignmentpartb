def convert_to_non_negative_coordinates(coordinates):
    # Find the minimum x-coordinate and minimum y-coordinate
    min_x = min(coord[0] for coord in coordinates)
    min_y = min(coord[1] for coord in coordinates)

    # Calculate the amount to add to make coordinates non-negative
    add_x = abs(min_x)
    add_y = abs(min_y)

    # Add the calculated amounts to all coordinates
    new_coordinates = [(coord[0] + add_x, coord[1] + add_y) for coord in coordinates]

    return new_coordinates

# Input coordinates
input_coordinates = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]

# Convert to non-negative coordinates
output_coordinates = convert_to_non_negative_coordinates(input_coordinates)

# Print the result
print(output_coordinates)
