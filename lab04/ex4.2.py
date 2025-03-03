import timeit
import random
import matplotlib.pyplot as plt

# Exercise 4

# 3.
# code for an inefficient implementation for searching a sorted array: linear search
def linearSearch(arr, key):
    for i in range(len(arr)): # iterates through array sequentially
        if arr[i] == key: # checks if element matches query key
            return i # returns element if match
    return -1 # if no match, return -1.

# code for an efficient implementation for searching an array: binary search
def binarySearch(arr, key, first, last):
    if first > last: # base case
        return -1  
    
    mid = (first + last) // 2  # Find the middle index and use integer div to get whole number
    
    if key == arr[mid]:
        return mid  # Key found at index mid
    elif key < arr[mid]:
        return binarySearch(arr, key, first, mid - 1)  # Search the left half
    else:
        return binarySearch(arr, key, mid + 1, last)  # Search the right half

# 4. 
# Worst-Case Complexity for Linear Search: O(n)
# occurs if the element to be searched for is the last element in the array.
#
#  Worst-Case Complexity for Binary Search: O(logn)
# occurs if the element to be searched for is the first or last element
# in the array or if the element does not exist in the array.


# 5.

arrLen = 1500 # make length of array 1500
arr = list(range(arrLen)) # list makes it sorted 
trials = 100

# lists to store execution times
linearTimes = []
binaryTimes = []

for _ in range(trials):
    # randomly assign the key to be one of the values in arr
    key = random.randint(0, arrLen - 1)

# Measure Linear Search using timeit
    linearTime = timeit.timeit(lambda: linearSearch(arr, key), number=1)
    linearTimes.append(linearTime)

    # Measure Binary Search using timeit
    binaryTime = timeit.timeit(lambda: binarySearch(arr, key, 0, arrLen - 1), number=1)
    binaryTimes.append(binaryTime)

# plot results
# Plot the results
plt.figure(figsize=(10, 5))
plt.hist(linearTimes, bins=30, alpha=0.5, label="Linear Search", color='red')
plt.hist(binaryTimes, bins=30, alpha=0.5, label="Binary Search", color='blue')
plt.xlabel("Time (seconds)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Execution Time Distribution: Linear vs. Binary Search")
plt.show()

'''
Binary Search (blue) has a much narrower and steeper distribution, meaning it consistently runs very quickly.
Linear Search (red) has a wider and more spread-out distribution, meaning execution times vary more depending on the position of the target.
'''