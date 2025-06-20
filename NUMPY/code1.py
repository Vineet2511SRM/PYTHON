import numpy as np

# Create two arrays
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([5, 15, 25, 35, 45])

# Perform element-wise arithmetic operations
addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

# Create a single dimensional array with integer values
integer_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Find mean, median and standard deviation
mean_value = np.mean(integer_array)
median_value = np.median(integer_array)
std_dev_value = np.std(integer_array)

# Create an array of random numbers between 100 and 200
random_numbers = np.random.randint(100, 200, size=10)

print(addition)
print(subtraction)
print(multiplication)
print(division)
print(mean_value)
print(median_value)
print(std_dev_value) 
print(random_numbers)
print(integer_array)