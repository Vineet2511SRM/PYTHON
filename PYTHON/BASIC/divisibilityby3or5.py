# Get input from the user
N = int(input("Enter a natural number (10 <= N <= 1000): "))

# Ensure the input is within the given constraints
if 10 <= N <= 1000:
    # Calculate the sum of multiples of 3 or 5 below N
    total = sum(i for i in range(N) if i % 3 == 0 or i % 5 == 0)
    print("The sum of multiples of 3 or 5 below", N, "is:", total)
else:
    print("Input out of bounds. Please enter a number between 10 and 1000.")

    # test comment
    