# Input
elements = tuple(map(int, input("Enter numbers separated by spaces: ").split()))

# Operations
max_value = max(elements)
min_value = min(elements)
total_sum = sum(elements)

# Output
print(f"Tuple: {elements}")
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
print(f"Sum of elements: {total_sum}")
