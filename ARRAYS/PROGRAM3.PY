# Input dimensions of the matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Initialize a 2D array (list of lists)
matrix = []
print("Enter the elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Transpose the matrix
transpose = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

# Output
print("Original Matrix:")
for i in matrix:
    print(i)

print("Transposed Matrix:")
for j in transpose:
    print(j)
