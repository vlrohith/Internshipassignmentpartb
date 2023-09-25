# Original matrices
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Sort a matrix based on the sum of its rows using Lambda
sort_matrix = lambda matrix: sorted(matrix, key=lambda row: sum(row))

# Sort and print the matrices
sorted_matrix1 = sort_matrix(matrix1)
sorted_matrix2 = sort_matrix(matrix2)

print("Original Matrix 1:", matrix1)
print("Sort the matrix 1 based on the sum of its rows:", sorted_matrix1)

print("Original Matrix 2:", matrix2)
print("Sort the matrix 2 based on the sum of its rows:", sorted_matrix2)
