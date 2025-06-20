n = int(input())  # Read input
if 1 <= n <= 1000:  # Check constraints
    result = 2 ** n  # Calculate 2^n
    result_str = str(result)  # Convert result to string
    digit_sum = 0  # Initialize sum of digits
    for digit in result_str:  # Iterate through each digit
        digit_sum += int(digit)  # Convert and add to sum
    print(digit_sum)  # Print result
else:
    print("Invalid input")  # Handle invalid input
