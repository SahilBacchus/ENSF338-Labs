import sys
import random
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

# bubble sort 
def bubble_sort(arr):
    n = len(arr)
    # outer loop loops through number of passes
    for i in range(n):
        # inner loop loops remaining unsorted portion of array
        for j in range(0, n-i-1):
            # if first element greater than the next element,
            # swap their positions
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


# quick sort
def quicksort(arr, low, high):
    # base case checks if low index is less than high index
    # if low >= high, means list is eother 0 or 1, meaning already sorted
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

# selects pivot element, rearranges array so that elements less than
# pivot are on the left and elements greater than pivot on the right
def partition(arr, low, high):
    # pivot chosen as the element at the low index of arr
    pivot = arr[low]
    # left starts from element after the pivot
    left = low + 1
    # right starts from high index
    right = high
    done = False # flag
    while not done:
        # moves left pointer to the right as long as 
        # element at arr[left] is smaller than or equal to pivot
        # and <= right pointer
        while left <= right and arr[left] <= pivot:
            left = left + 1
        # moves right pointer to the left
        while arr[right] >= pivot and right >= left:
            right = right - 1
        # if right pointer has passed the left pointer, done 
        # flag is set to true 
        if right < left:
            done = True
        else:
            # swap via arr[left] and arr[right] via tuple unpacking
            arr[left], arr[right] = arr[right], arr[left]
    # place pivot in correct position by swapping arr[low] and arr[right]
    arr[low], arr[right] =arr[right], arr[low]
    return right
    # return right index, which is now the position of pivot element in sorted array
    # value will be used to divide array int0 2 parts for more recursive sorting
def

def test_and_time_sorts():
    # created array containing various input sizes
    sizes = [0, 5, 10, 15, 20, 25, 30, 35, 40, 100, 150, 300, 400, 700, 1000, 2000, 5000, 10000, 15000, 19000]
    bubblesort_times = []
    quicksort_times = []


'''import random
import time
import matplotlib.pyplot as plt

# Quicksort Algorithm
def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization: stop if no elements were swapped

# Function to generate random arrays of a given size
def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]

# Function to generate best case for Bubble Sort (already sorted)
def generate_best_case_bubble_sort(size):
    return list(range(1, size+1))

# Function to generate worst case for Bubble Sort (reverse sorted)
def generate_worst_case_bubble_sort(size):
    return list(range(size, 0, -1))

# Function to generate best case for Quicksort (sorted)
def generate_best_case_quick_sort(size):
    return list(range(1, size+1))

# Function to generate worst case for Quicksort (reverse sorted)
def generate_worst_case_quick_sort(size):
    return list(range(size, 0, -1))

# Function to test both algorithms on different scenarios
def test_sorting_algorithms():
    sizes = [10, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 60000, 70000]
    
    quicksort_best_times = []
    bubble_sort_best_times = []
    
    quicksort_worst_times = []
    bubble_sort_worst_times = []
    
    quicksort_avg_times = []
    bubble_sort_avg_times = []
    
    for size in sizes:
        # Best-case scenario
        best_case_quick = generate_best_case_quick_sort(size)
        best_case_bubble = generate_best_case_bubble_sort(size)
        
        start_time = time.time()
        quicksort(best_case_quick, 0, len(best_case_quick) - 1)
        quicksort_best_times.append(time.time() - start_time)

        start_time = time.time()
        bubble_sort(best_case_bubble)
        bubble_sort_best_times.append(time.time() - start_time)

        # Worst-case scenario
        worst_case_quick = generate_worst_case_quick_sort(size)
        worst_case_bubble = generate_worst_case_bubble_sort(size)

        start_time = time.time()
        quicksort(worst_case_quick, 0, len(worst_case_quick) - 1)
        quicksort_worst_times.append(time.time() - start_time)

        start_time = time.time()
        bubble_sort(worst_case_bubble)
        bubble_sort_worst_times.append(time.time() - start_time)

        # Average-case scenario (random case)
        avg_case_quick = generate_random_array(size)
        avg_case_bubble = avg_case_quick[:]

        start_time = time.time()
        quicksort(avg_case_quick, 0, len(avg_case_quick) - 1)
        quicksort_avg_times.append(time.time() - start_time)

        start_time = time.time()
        bubble_sort(avg_case_bubble)
        bubble_sort_avg_times.append(time.time() - start_time)

    return sizes, quicksort_best_times, bubble_sort_best_times, quicksort_worst_times, bubble_sort_worst_times, quicksort_avg_times, bubble_sort_avg_times

# Run the tests
sizes, quicksort_best_times, bubble_sort_best_times, quicksort_worst_times, bubble_sort_worst_times, quicksort_avg_times, bubble_sort_avg_times = test_sorting_algorithms()

# Plot the results
plt.figure(figsize=(14, 10))

# Best-case performance
plt.subplot(2, 3, 1)
plt.plot(sizes, quicksort_best_times, label='Quicksort (Best)', color='b', marker='o')
plt.plot(sizes, bubble_sort_best_times, label='Bubble Sort (Best)', color='r', marker='x')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Best-Case Performance')
plt.legend()
plt.grid(True)

# Worst-case performance
plt.subplot(2, 3, 2)
plt.plot(sizes, quicksort_worst_times, label='Quicksort (Worst)', color='b', marker='o')
plt.plot(sizes, bubble_sort_worst_times, label='Bubble Sort (Worst)', color='r', marker='x')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Worst-Case Performance')
plt.legend()
plt.grid(True)

# Average-case performance
plt.subplot(2, 3, 3)
plt.plot(sizes, quicksort_avg_times, label='Quicksort (Average)', color='b', marker='o')
plt.plot(sizes, bubble_sort_avg_times, label='Bubble Sort (Average)', color='r', marker='x')
plt.xlabel('Array Size')
plt.ylabel('Time (seconds)')
plt.title('Average-Case Performance')
plt.legend()
plt.grid(True)

# Display the plots
plt.tight_layout()
plt.show()
'''