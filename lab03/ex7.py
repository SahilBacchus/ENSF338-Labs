import sys
import json
import matplotlib.pyplot as plt
import timeit
import random

sys.setrecursionlimit(20000)


with open('lab03/lab_data/ex7data.json', 'r', encoding='UTF-8') as infile: 
    data = json.load(infile)



def binarySearch(arr, first, last, key):
    if (first <= last):
        mid = (first + last) // 2 
        
        if arr[mid] == key:
            return mid
        
        elif key < arr[mid]:
            return binarySearch(arr, first, mid - 1, key)
        
        else:
            return binarySearch(arr, mid + 1, last, key)
    
    return -1


def binarySearchConfig(arr, first, last, key, mid):
    if (first <= last):
        #mid = input("Enter midpoint for first iteration:")
        
        if arr[mid] == key:
            return mid
        
        elif key < arr[mid]:
            return binarySearch(arr, first, mid - 1, key)
        
        else:
            return binarySearch(arr, mid + 1, last, key)
    
    return -1

def timerForBinSearch(arr, last, key, mid):
    timer = timeit.Timer(lambda: binarySearchConfig(arr, 0, last, key, mid))
    time = timer.timeit(number=1)
    return time

time_results = []
midpoints = []

for i in range(0, len(data), 1000):   
    key = random.randint(0, 999998)
    time_taken = timerForBinSearch(data, len(data) - 1, key, i)
    if(time_taken < 0.00001):
        midpoints.append(i)
        time_results.append(time_taken)


plt.figure(figsize=(10, 6))
plt.scatter(midpoints, time_results, color='blue', label='Search Time')
plt.xlabel('Initial Midpoint')
plt.ylabel('Search Time (seconds)')
plt.title('Effect of Initial Midpoint on Binary Search Performance')
plt.grid(True)
plt.savefig('lab03/output_5.png')
plt.show()





infile.close()




