# Question: Replace all odd numbers in arr with -1 without changing arr
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: out
# array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Solution
import numpy as npy
arr = npy.arange(10)

out = arr.copy()

out[out%2 == 1] = -1

print('Modified Array')
print(out)

print('\nOriginal Array')
print(arr)