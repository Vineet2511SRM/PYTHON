# Input
set1 = set(map(int, input("Enter elements of first set separated by spaces: ").split()))
set2 = set(map(int, input("Enter elements of second set separated by spaces: ").split()))

# Operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

# Output
print(f"Union: {union_set}")
print(f"Intersection: {intersection_set}")
