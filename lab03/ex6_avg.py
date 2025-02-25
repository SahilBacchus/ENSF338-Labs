import numpy as np
import timeit
import matplotlib.pyplot as plt
import random



######################################################################################
#-- First, implement both algorithms [0.1 pts] --------------------------------------#
######################################################################################

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i 
    return -1





def partition(arr, low, high): # We chose the pivot as the last element and move everything smaller to the left
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1 
     

def quicksort(arr, low, high):
    if low < high: 
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot-1)
        quicksort(arr, pivot+1, high)


def binary_search(arr, key, first, last):
    if (first <= last):
        mid = (first + last) // 2  
        if arr[mid] == key:
            return mid      
        elif key < arr[mid]:
            return binary_search(arr, key, first, mid - 1) 
        else:
            return binary_search(arr, key, mid + 1, last)
    return -1



def quicksort_then_binary_search(arr, key, size):
    first = 0
    last = size - 1
    quicksort(arr, first, last)
    binary_search(arr, key, first, last)
    


######################################################################################
#-- Then, measure their performance on 100 random tasks. An appropriate random task -#
#-- here would be to search for a constant element in an array that gets reshuffled -#
#-- every time [0.1 pts] ------------------------------------------------------------#
######################################################################################

def create_array(size):
    arr = np.random.randint(1, size, size=size)  
    return arr

def time_linear_search(arr, tasks=100, key=21): 
    times = []
    for i in range(tasks):
        random.shuffle(arr) 
        time = timeit.timeit(lambda: linear_search(arr, key), number=10)
        times.append(time / 10)
    avg_time = sum(times) / len(times)
    print(f"Linear Search time for {len(arr)}: {avg_time}")
    return avg_time    


def time_quicksort_then_binary_sort(arr, size, tasks=100, key=21): 
    times = []
    for i in range(tasks):
        random.shuffle(arr) 
        time = timeit.timeit(lambda: quicksort_then_binary_search(arr, key, size), number=1)
        times.append(time / 1)
    avg_time = sum(times) / len(times)
    print(f"Quicksort then Binary Search time for {len(arr)}: {avg_time}")
    return avg_time  

print("running question 2: ")
arr = create_array(1000)
time_linear_search(arr)
time_quicksort_then_binary_sort(arr, 1000)






######################################################################################
#-- You must redo the above with inputs of size 10, 20, 50, 100, 200, 500, 1000, ----#
#-- 2000, 5000, 10000 [0.2 pts] -----------------------------------------------------#
######################################################################################


sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000]
sizes = np.array(sizes)

ls_times = []
qbs_times = []

print("\n\nrunning tests: ")
for size in sizes:
    arr_0 = create_array(size)
    arr_1 = arr_0.copy()
    ls_times.append(time_linear_search(arr_0))
    qbs_times.append(time_quicksort_then_binary_sort(arr_1, size=size))




######################################################################################
#-- Plot the above and discuss which algorithm is faster [0.1 pts] ------------------#
######################################################################################

plt.figure(figsize=(10, 6))

# Plot the raw timing data
plt.scatter(sizes, ls_times, color='blue', label='Linear Search')
plt.scatter(sizes, qbs_times, color='red', label=' Quicksort then Binary Sort')

plt.xlabel('Array Size')
plt.ylabel('Time')
plt.title('Linear Search vs. Quicksort then Binary Sort  Times - Avg Case')
plt.legend()
plt.grid(True)
plt.savefig('lab03/output.6_avg.png')
plt.show()


'''
Linear Search is FASTER, this is due to how the experiment is run since we mitigate any of
the gains that binary search may yeild due to the fact that we are incurring a heavy sorting 
computation each time. The only way that quicksort then binary search could be faster is if 
we sort once and run the search multiple times on that sorted array. 

Time Complexity for this Experiment: 
    Linear Search: O(N)

    Quicksort then Binary Search: O(N*log(N)) + O(log(N)) = O(N*log(N))


'''
