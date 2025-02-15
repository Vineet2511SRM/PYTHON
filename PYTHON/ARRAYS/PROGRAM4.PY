# Input dimensions of the matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize a 2D array (list of lists)
matrix = []
print("Enter the elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Flatten the matrix into a 1D array
flattened_array = []
for row in matrix:
    flattened_array.extend(row)  # Add each row's elements to the flattened array

# Output the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Output the flattened array
print("Flattened Array:")
print(flattened_array)
