#slicing single element
import numpy as np
list = [1,2,3,4,5,6]
a = np.array(list)
print(a[3])
#slicing using start stop
print(a[0:3])
#slicing using start,end,and step by skipping in between elements
print(a[0:5:2])
#slicing using only start position
print(a[3:])
#slicing using only stop position
print(a[:4])
#slicing without any index
print(a[:])
#slicing using negative index
print(a[-4:-2])
#reversing numpy array
print(a[::-1])
