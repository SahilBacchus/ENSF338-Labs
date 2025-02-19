import random
import matplotlib.pyplot as plt
import numpy as np

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

sizes = list(range(10, 501, 20)) 
comp_counts = []
swap_counts = []

for size in sizes:
    arr = [random.randint(1, 1000) for _ in range(size)]
    comparisons, swaps = bubble_sort(arr[:])
    comp_counts.append(comparisons)
    swap_counts.append(swaps)

comp_fit = np.polyfit(sizes, comp_counts, 2)
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

plt.tight_layout()
plt.show()
