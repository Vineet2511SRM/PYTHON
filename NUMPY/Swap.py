# Question: Swap columns 1 and 2 in the array arr.

# Input:
import numpy as np
arr = np.arange(9).reshape(3,3)

print('Original array')
print(arr)

# Solution

print("\nModified array")
print(arr[:, [1,0,2]])