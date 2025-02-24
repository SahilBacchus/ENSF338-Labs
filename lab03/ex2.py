import sys
import random
import timeit
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)

# bubble sort 
def bubble_sort(arr):
    n = len(arr)
    # outer loop loops through number of passes
    for i in range(n):
        swapped = False
        # inner loop loops remaining unsorted portion of array
        for j in range(0, n-i-1):
            # if first element greater than the next element,
            # swap their positions
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 
                swapped = True
        if not swapped:
            break
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




# generate best case for quick sort
def generate_best_case_quick_sort(n):
    if n == 0:
        return []
    if n == 1:
        return[0]
    mid = n // 2
    left = generate_best_case_quick_sort(mid)
    right = generate_best_case_quick_sort(n - mid - 1)
    return left + [mid] + right


# 20 different input sizes, starting from size 10 to 110, going up by 5 each time
input_sizes = list(range(10, 110, 5))
# input_sizes = list(range(10, 2100, 100))
# cases list containing best worst and average
cases = ["Best", "Worst", "Average"]

# dictionaries for bubble and quick sort and hybrid sort to store results
bubble_sort_times = {case: [] for case in cases}
quick_sort_times = {case: [] for case in cases}

# performance tests
for n in input_sizes:
    for case in cases:
        if case == "Best":
            # best case for bubble sort is a sorted array
            test_array_bubble = list(range(n))
            # best case for quick sort is when the pivots
            # always create equal sized subarrays
            test_array_quick = generate_best_case_quick_sort(n)

        elif case == "Worst":
            # worst case for bubble is reversed order
            test_array_bubble = list(range(n, 0, -1))
            # worst case for quicksort: already sorted or reverse sorted array
            test_array_quick = list(range(n))

        elif case == "Average":
            # Average case for bubble and quick:
            # random order for both
            # _ in for loop means to ignore loop variable (it doesn't matter)
            test_array_bubble = [random.randint(0, n) for _ in range(n)]
            test_array_quick = test_array_bubble.copy()

        # measure bubble sort performance via timeit
        # number=10 / 10 used to average timing over multiple runs to smooth out noise
        elapsed_time_bubble = timeit.timeit(lambda: bubble_sort(test_array_bubble.copy()), number=10) / 10
        bubble_sort_times[case].append(elapsed_time_bubble)

        # measure quick sort performance vai timeit
        elapsed_time_quick = timeit.timeit(lambda: quicksort(test_array_quick.copy(), 0, len(test_array_quick) - 1), number=10) / 10
        quick_sort_times[case].append(elapsed_time_quick)

        


# Plot Results
for case in cases:
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, bubble_sort_times[case], label='Bubble Sort', marker='o')
    plt.plot(input_sizes, quick_sort_times[case], label='In-place Quick Sort', marker='x')
    plt.title(f'{case} Case Performance')
    plt.xlabel('Input Size')
    plt.ylabel('Time (seconds)')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'lab03/output.2_{case}.png')
    plt.show()
