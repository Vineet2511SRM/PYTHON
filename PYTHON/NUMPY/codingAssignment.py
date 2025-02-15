import numpy as np
myArray = np.array([[11,12,13],[14,15,16],[17,18,19]])
#getting subarray of first row and first 2 columns
print(myArray[:1,:2])
#chaning all elements in 1st and second row to 0

print(myArray[:,[0,2]])
print(myArray[1,:])