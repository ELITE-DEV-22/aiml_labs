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

print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1/arr2)

#slicing
weather = np.array([
    [1, 26],
    [2, 28],
    [3, 28],
])


# weather [:,1]#takes all rows and column 1
index = np.argmin(weather[:,1])
date = weather[index, 0]
temp = weather[index, 1]
print(f"hottest day is on {date} with a temperature of {temp}")
