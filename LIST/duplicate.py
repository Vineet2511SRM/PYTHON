# Initial list with duplicates
L1 = [1, 2, 3, 2, 4, 5, 5, 6, 7, 3]

# Removing duplicates by converting the list to a set and then back to a list
L2 = list(set(L1))

# Output the result
print("List after removing duplicates:", L2)
