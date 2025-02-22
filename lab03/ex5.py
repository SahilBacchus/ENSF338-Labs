import numpy as np
import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# NOTE: due to the large array sizes chosen for visualization purposes the code may take >1 min to run



######################################################################################
#-- Implement both “traditional” insertion sort and binary insertion sort [0.3 pts] -#
######################################################################################

# Traditional insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]
        j = i-1
        # Linear search to find where element should be inserted and move all elements 
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key





# Binary insertion sort --> like insertion sort but uses binary search to to find where an element should be sorted
def binary_search(arr, key, first, last):
    if (first <= last):
        mid = (first + last) // 2  
        if arr[mid] == key:
            return mid      
        elif key < arr[mid]:
            return binary_search(arr, key, first, mid - 1) 
        else:
            return binary_search(arr, key, mid + 1, last)
    return first

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        loc = binary_search(arr, key, 0, j)
        # Move all elements
        while j >=  loc:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key





####################################################################################
#-- Devise and run an experiment where you test each algorithm on a number of -----#
#-- average-case inputs of increasing length [0.3 pts] ----------------------------#
####################################################################################

def create_arrays(size):
    arr = np.random.randint(1, size, size=size)  
    return arr

def time_insertion_sort(arr, number=100): 
    time = timeit.timeit(lambda: insertion_sort(arr), number=number)
    avg_time = time / number
    print(f"Insertion time for {len(arr)}: {avg_time}")
    return avg_time    

def time_binary_insertion_sort(arr, number=100): 
    time = timeit.timeit(lambda: binary_insertion_sort(arr), number=number)
    avg_time = time / number
    print(f"Binary insertion time for {len(arr)}: {avg_time}")
    return avg_time 

sizes = [10, 50, 100, 500, 1000, 2000, 4000, 8000, 16000, 32000]
sizes = np.array(sizes)

is_times = []
bis_times = []

print("running tests: ")
for size in sizes:
    arr_0 = create_arrays(size)
    arr_1 = arr_0.copy()
    is_times.append(time_insertion_sort(arr_0, 1))
    bis_times.append(time_binary_insertion_sort(arr_1, 1))

print(f"insertion times: {is_times}")
print(f"binary insertion times: {bis_times}")






#####################################################################################
#-- Plot the results of both algorithms within the same plot, together with --------#
#-- appropriate interpolating functions [0.2 pts] ----------------------------------#
#####################################################################################

def quadratic_func(x, a, b):
    return a*x**2 + b


popt_is, _ = curve_fit(quadratic_func, sizes, is_times) # We know insertion sort is O(N^2) so we fit it to a quadratic function
popt_bis, _ = curve_fit(quadratic_func, sizes, bis_times )# We know binary insertion sort is O(N^2) so we fit it to a quadratic function


plt.figure(figsize=(10, 6))

# Plot the raw timing data
plt.scatter(sizes, is_times, color='blue', label='Traditional Insertion Sort')
plt.scatter(sizes, bis_times, color='red', label='Binary Insertion Sort')

# Plot the fitted curves
plt.plot(sizes, quadratic_func(sizes, *popt_is), 'b--', label=f"Quadratic curve: {popt_is[0]:.2e}*n^2 + {popt_is[1]:.2e} ")
plt.plot(sizes, quadratic_func(sizes, *popt_bis), 'r--', label=f"Quadratic curve: {popt_bis[0]:.2e}*n^2 + {popt_bis[1]:.2e}")

plt.xlabel('Array Size')
plt.ylabel('Time')
plt.title('Insertion Sort vs. Binary Insertion Sort  Times')
plt.legend()
plt.grid(True)
plt.savefig('lab03/output.5.png')









#####################################################################################
#-- Discuss the results: which algorithm is faster? Why? [0.2 pts] -----------------#
#####################################################################################
'''
While both algorithms exhibit a Average and Worst-Case time complexity of O(N^2), 
there lies differences in there comparative step: 

Insertion Sort: requires O(N)  time to find the location where an element needs to be 
                inserted as it uses linear search to do so

    Vs.

Binary Insertion SOrt: requires O(log(N)) time to find the location where an element 
                       needs to be inserted as it uses binary search to do so

However, due to the shifting of elements the overall time complexity for both remain O(N^2). 
But due to the performance improvement in the comparisons, in practice Binary Insertion Sort 
is FASTER than Insertion Sort. 


'''


