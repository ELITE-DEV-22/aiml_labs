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
index1 = np.argmin(weather[:,1])
date1 = weather[index1, 0]
temp1 = weather[index1, 1]
print(f"coldest day is on {date1} with a temperature of {temp1}")

index2 = np.argmax(weather[:,1])
date2 = weather[index2, 0]
temp2 = weather[index2, 1]
print(f"coldest day is on {date2} with a temperature of {temp2}")
