# Input dimensions
r = int(input())
c = int(input())

# Create a list to store the input numbers
matrix = []
for _ in range(r * c):
    num = int(input())
    matrix.append(num)

# Rearrange elements into the required column-wise format
result = []
for i in range(r):
    row = []
    for j in range(i, len(matrix), r):
        row.append(matrix[j])
    result.append(row)

# Print the output in the required format
for row in result:
    print(*row,"")