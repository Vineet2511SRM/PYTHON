# Question: Get all items between 5 and 10 from a.

# Input: a = np.array([2, 6, 1, 9, 10, 3, 27])
# Output: (array([6, 9, 10]),)


# Solution
import numpy as np
a = np.array([2, 6, 1, 9, 10, 3, 27])
print(a[(a >= 5) & (a <= 10)])