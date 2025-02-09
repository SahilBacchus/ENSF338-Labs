import numpy as np
import pandas as pd
import timeit
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def linear_search(sorted_vector, size, key):
    for i in range(0,size):
        if(key == sorted_vector[i]):
            return i
    return -1


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



def generate_and_sort_vector(size):
    vector = np.random.randint(1,size, size=size)  
    sorted_vector = sorted(vector)  
    return sorted_vector

def time_computation_ls(sorted_vector, size):
    timer = timeit.Timer(f"linear_search({sorted_vector},{size},{size/2})", setup="from __main__ import linear_search")
    total_time = timer.timeit(number=100)
    print(f"Linear Search Time (For {size}): {total_time} seconds")
    return total_time

def time_computation_bs(sorted_vector, size):
    timer = timeit.Timer(f"binarySearch({sorted_vector},{0},{size},{size/2})", setup="from __main__ import binarySearch")
    total_time = timer.timeit(number=100)
    print(f"Binary Search Time (For {size}): {total_time} seconds")
    return total_time


sizes = [1000, 2000, 4000, 8000, 16000, 32000]
sizes = np.array(sizes)
ls_times = []
bs_times = []

for size in sizes:
    sorted_vector = generate_and_sort_vector(size)  # Generate and sort the vector
    ls_times.append(time_computation_ls(sorted_vector, size))
    bs_times.append(time_computation_bs(sorted_vector, size))



#------------------- Question 3 ----------------------------#
def linear_func(x, a, b):
    return a*x + b

def log_func(x, a, b):
    return a*np.log(x) + b

popt_ls, _ = curve_fit(linear_func, sizes, ls_times) # We know linear search is O(N) so we fit it to a linear function
popt_bs, _ = curve_fit(log_func, sizes, bs_times )# We know binary search is O(log(N)) so we fit it to a log function


plt.figure(figsize=(10, 6))

# Plot the raw timing data
plt.scatter(sizes, ls_times, color='blue', label='Linear Search Data')
plt.scatter(sizes, bs_times, color='red', label='Binary Search Data')

# Plot the fitted curves
plt.plot(sizes, linear_func(sizes, *popt_ls), 'b--', label=f"Linear line: {popt_ls[0]:.2e}*n + {popt_ls[1]:.2e}")
plt.plot(sizes, log_func(sizes, *popt_bs), 'r--', label=f"Log curve: {popt_bs[0]:.2e}*log(n) + {popt_bs[1]:.2e}")

plt.xlabel('Vector Size')
plt.ylabel('Time')
plt.title('Linear Search vs. Binary Search Times')
plt.legend()
plt.grid(True)
plt.savefig('lab02/output.5.png')


#------------------- Question 4 ----------------------------#

print("----------------------------")
print(f"Linear Search --> Linear line: {popt_ls[0]:.2e}*n + {popt_ls[1]:.2e}")
print(f"Binary Search --> Log curve: {popt_bs[0]:.2e}*log(n) + {popt_bs[1]:.2e}")

'''
Print statement output: 
Linear Search --> Linear line: 1.91e-06*n + 3.35e-03
Binary Search --> Log curve: 2.64e-03*log(n) + -1.99e-02




For the LInear Search we fitted a linear line of form a*x + b.
where, 
a = 1.91e-06
b = 3.35e-03
which was to be expected as the linear searh algorithm has to perform n operations 
as it has to loop through the entire array to find the key.


For the Binary Search we fitted a logrithmic curve of form a*log(n) + b.
where, 
a = 2.64e-03
b = -1.99e-02
which was to be expected as the binary searh algorithm has to perform log_2(n) operations 
as it removes half the array from its search each time. Resulting in the large performance 
gain compared to linear search as seen in the graph. 



'''