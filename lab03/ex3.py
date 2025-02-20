import random
import matplotlib.pyplot as plt
import numpy as np


"""
Note: Use this to change to the proper directory if it doesn't
      automatically make the directory lab03

import os
print("Current Working Directory:", os.getcwd())
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)"""


def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(n - i - 1):
            comparisons += 1 
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
                swaps += 1
    return comparisons, swaps

sizes = (range(10, 501, 20))#Creating list through sizes 10 to 500
comp_counts = []
swap_counts = []

for size in sizes:#Iterating through sizes 10 to 500
    arr = [random.randint(1, 1000) for i in range(size)]#Adding random numbers to array
    comparisons, swaps = bubble_sort(arr[:])
    comp_counts.append(comparisons)#Adding comparisons to list
    swap_counts.append(swaps)#Adding swap to list


#Plotting
comp_fit = np.polyfit(sizes, comp_counts, 2)#fitting
swap_fit = np.polyfit(sizes, swap_counts, 2)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(sizes, comp_counts, label='Observed Comparisons', color='b')
plt.plot(sizes, np.polyval(comp_fit, sizes), 'r--', label=f'Fit: {comp_fit[0]:.2e}n^2')
plt.xlabel('Input Size')
plt.ylabel('# Comparisons')
plt.legend()
plt.title('Bubble Sort Comparisons')



plt.subplot(1, 2, 2)
plt.scatter(sizes, swap_counts, label='Observed Swaps', color='g')
plt.plot(sizes, np.polyval(swap_fit, sizes), 'r--', label=f'Fit: {swap_fit[0]:.2e}n^2')
plt.xlabel('Input Size')
plt.ylabel('# Swaps')
plt.legend()
plt.title('Bubble Sort Swaps')
#plt.savefig('Comparison_Swaps.png')


plt.tight_layout()
plt.show()
