import numpy as np

arr = np.array([1,2,3,4,5])
print(arr)

# np.arange(start, stop)
b = np.arange(1,15) #prints values from 1-14 in ascending order
print(b)

#np.arange(start, stop, step)
c = np.arange(1,15,2)
print(c)

#2-d array
arr1 = np.array([
    [1,2],
    [3,4]
])
print(arr1)

arr2 = np.array([
    [5,5],
    [9,6]
])

print(arr2)