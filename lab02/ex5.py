import numpy as np
import pandas as pd
import time

v = [1,2,3]

def linear_search(sorted_vector, size, key):
    for i in range(0,size):
        if(key == sorted_vector[i]):
            return i
    return -1
s

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

sizes = [1000, 2000, 4000, 8000, 16000, 32000]
sort_times = {}

for size in sizes:
    #start_time = time.time()  # Start the timer
    sorted_vector = generate_and_sort_vector(size)  # Generate and sort the vector
    end_time = time.time()  # End the timer
    #np.savetxt(f'data{size}.txt', sorted_vector)
    #sort_times[size] = end_time - start_time  # Store the time taken to sort

# Print the sorting times for each vector size
#for size, sort_time in sort_times.items():
    #print(f"Time taken to sort a vector of size {size}: {sort_time:.6f} seconds")

print(binarySearch(v, 0, 2, 4))
