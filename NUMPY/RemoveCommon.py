# Question: From array a remove all items present in array b

# Input: a = np.array([1,2,3,4,5])
#        b = np.array([5,6,7,8,9])

# Output: array([1,2,3,4])


# Solution
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

print(np.setdiff1d(a,b))