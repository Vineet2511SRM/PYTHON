# Input from the user
n = int(input("Enter a number: "))

# Generating the pattern
for i in range(1, n + 1):
    for j in range(1, i+1):
        # Print odd numbers if it's the last row or an odd row, even numbers otherwise
        if i % 2 == 1 or i == n:  # Odd rows or the last row
            print(j * 2 - 1, end=" ")
        else:  # Even rows
            print(j * 2, end=" ")
    print()  # Move to the next line after each row
