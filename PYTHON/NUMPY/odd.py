# Question : Extract all odd numbers from array
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([1, 3, 5, 7, 9])
import numpy as np

arr = np.arange(10)
x = arr[arr%2 == 1]
print(f"Odd numbers from array {arr:} are :",x)