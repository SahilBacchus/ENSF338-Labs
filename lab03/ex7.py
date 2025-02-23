import sys
import json
import matplotlib.pyplot as plt
import timeit



"""
Comments on the graph: The initial midpoint clearly does
affect the Binary Search Performance of the list as 
the closer the intial point is to the target the faster it
can locate it.

Note: Use this to change to the proper directory if it doesn't
      automatically make the directory lab03
import os
print("Current Working Directory:", os.getcwd())
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)"""

sys.setrecursionlimit(20000)

with open('lab_data/ex7data.json', 'r', encoding='UTF-8') as infile:
    data = json.load(infile)

with open('lab_data/ex7tasks.json', 'r', encoding='UTF-8') as infile:
    search_tasks = json.load(infile)

def binarySearchConfig(arr, first, last, key, mid):
    if first <= last:
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            return binarySearchConfig(arr, first, mid - 1, key, (first + mid - 1) // 2)
        else:
            return binarySearchConfig(arr, mid + 1, last, key, (mid + 1 + last) // 2)
    return -1  # Not found

def timerForBinSearch(arr, last, key, mid):
    timer = timeit.Timer(lambda: binarySearchConfig(arr, 0, last, key, mid))
    return timer.timeit(number=1)


time_results = []
midpoints = []
last_index = len(data) - 1

for key in search_tasks[:100]:
    best_time = float("inf")
    best_mid = None

    for i in range(0, len(data), 1000):  
        time_taken = timerForBinSearch(data, last_index, key, i)

        if time_taken < best_time:
            best_time = time_taken
            best_mid = i

    midpoints.append(best_mid)
    time_results.append(best_time)

plt.figure(figsize=(10, 6))
plt.scatter(search_tasks[:100], midpoints, color='blue', label='Best Initial Midpoint')
plt.xlabel('Search Task (Target Number)')
plt.ylabel('Best Initial Midpoint')
plt.title('Effect of Initial Midpoint on Binary Search Performance')
plt.grid(True)
plt.legend()
#plt.savefig('output_7.png')
plt.show()
