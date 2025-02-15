import numpy as np
a = np.array([1,2,3,4,5])
print(a)
#dtype
print(a.dtype)#dtype = int64
#creating multidimensional array using lists
a = np.array(([2,3,4],[4,5,6],[6,7,8]))
print(a)
#creating numpy array using functions
a = np.arange(10)
b = np.arange(10,20)
c = np.arange(1,20,2)
print(a)
print(b)
print(c)
#mdim arrays with np.zeroes
a = np.zeros((2,3))
print(a)
b = np.zeros_like(a)
print(b)
#np.ones will create an array filled with 1 values
#default dtype for both is float64
#creating an array filled with specified value
a=np.full((3,3),3.14)
print(a)
#creatingrandomnumpyvalues
a = np.random.random((3,3))
print(a)
a = np.random.randint(0,10,(3,3))
print(a)

