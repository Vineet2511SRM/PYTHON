#Array attributes are properties of NumPy arrays that provide information about the array's shape, size, data type, dimension, and so on. 
import numpy as np

a = np.array(([2,4,6],[1,3,5],[9,6,9]))
print("Dimension:",a.ndim)
print("Shape:",a.shape)
print("Size:",a.size)
print("Data type:",a.dtype)
print("Size of each element:",a.itemsize)
print("Memory location: ",a.data)