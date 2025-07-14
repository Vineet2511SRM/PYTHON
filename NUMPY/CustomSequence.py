# Question: Create the following pattern without hardcoding. Use only numpy functions and the below input array a.

# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])


# Solution
import numpy as np
a = np.array([1,2,3])
x = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(x)
