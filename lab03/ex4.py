import sys
import time
import random
import numpy as np
import matplotlib.pyplot as plt

"""
Note: Use this to change to the proper directory if it doesn't
      automatically make the directory lab03

import os
print("Current Working Directory:", os.getcwd())
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)"""

sys.setrecursionlimit(20000)


def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high): 
    pivot = arr[low] #Pivot is not middle or median of three to show worst-case
    left = low + 1 
    right = high 
    done = False 
    while not done: 
        while left <= right and arr[left] <= pivot: 
            left = left + 1 
        while arr[right] >= pivot and right >=left: 
            right = right - 1 
        if right <left: 
            done= True 
        else: 
            arr[left], arr[right] = arr[right], arr[left] 
    arr[low], arr[right] = arr[right], arr[low] 
    return right

sizes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
times = []

for n in sizes:
    worst_case_input = list(range(n, 0, -1))#Creates list of deincrementing values
    start_time = time.time()#timing
    quicksort(worst_case_input, 0, len(worst_case_input)-1)
    end_time = time.time()
    times.append(end_time - start_time)

time_fit = np.polyfit(sizes, times, 2)#fitting

plt.figure(figsize=(10, 5))
plt.scatter(sizes, times, label='Measured Time')
plt.plot(sizes, np.polyval(time_fit, sizes), 'b--', label=f'Fit: {time_fit[0]:.2e}n^2')
plt.xlabel('Input Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Quicksort Worst-Case Complexity')
plt.legend()
plt.savefig('lab03/output.4.png')
plt.show()

