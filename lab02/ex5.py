import numpy as np
import pandas as pd
import timeit

v = [1,2,3]

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

def time_computation_bs(sorted_vector, size):
    timer = timeit.Timer(f"binarySearch({sorted_vector},{0},{size},{size/2})", setup="from __main__ import binarySearch")
    total_time = timer.timeit(number=100)
    print(f"Binary Search Time (For {size}): {total_time} seconds")

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
sort_times = {}

for size in sizes:
    #start_time = time.time()  # Start the timer
    sorted_vector = generate_and_sort_vector(size)  # Generate and sort the vector
    time_computation_ls(sorted_vector, size)
    time_computation_bs(sorted_vector, size)
    #np.savetxt(f'data{size}.txt', sorted_vector)
    #sort_times[size] = end_time - start_time  # Store the time taken to sort

# Print the sorting times for each vector size
#for size, sort_time in sort_times.items():
    #print(f"Time taken to sort a vector of size {size}: {sort_time:.6f} seconds")

