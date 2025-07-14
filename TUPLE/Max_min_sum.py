# Input
Elements = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

# Operations
max_value = max(Elements)
min_value = min(Elements)
total_sum = sum(Elements)

# Output
print(f"Tuple: {Elements}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of elements: {total_sum}")
