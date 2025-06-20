import numpy as np
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
def pair_max(x, y):
    # here I am using map to make tuple from a and b, other solution is using zip(a,b)
    maximum = [maxx(a,b) for a,b in map(lambda a,b:(a,b),x,y)]
    # using zip
    # maximum = [maxx(a,b) for a,b in zip(x,y)]
    return np.array(maximum)

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(a,b))