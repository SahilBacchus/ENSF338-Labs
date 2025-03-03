import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


""" 
Answer to Question 4: Binary Search for a Linked List unlike an array,
requires to first go "travel" through the list in order to find the
mid point. This causes a time complexity of O(n) prior to even doing
the search as you have to search for the mid point in order to use
binary search. In my opinion it is almost like using linear search
to search for the midpoint in order to use binary search. Therefore, 
to me it's logical to conclude that the time complexity of binary 
search on a linked list is n + log(n) which simplifies to O(n).
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if not self.head:
            self.head = Node(value)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(value)
    
    def binary_search(self, target):
        left, right = 0, self.length() - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = self.get_value_at(mid)
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def get_value_at(self, index):
        current = self.head
        for _ in range(index):
            if current:
                current = current.next
        return current.value if current else None

class Array:
    def __init__(self):
        self.data = []
    
    def append(self, value):
        self.data.append(value)
    
    def binary_search(self, target):
        left, right = 0, len(self.data) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.data[mid] == target:
                return True
            elif self.data[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

def measure_performance():
    sizes = [1000, 2000, 4000, 8000]
    linked_list_times = []
    array_times = []
    
    for size in sizes:
        linked_list = LinkedList()
        array = Array()
        
        for i in range(size):
            linked_list.append(i)
            array.append(i)
        
        target = size // 2
        
        # Measure time for Linked List binary search
        start = time.time()
        linked_list.binary_search(target)
        linked_list_times.append(time.time() - start)
        
        # Measure time for Array binary search
        start = time.time()
        array.binary_search(target)
        array_times.append(time.time() - start)
    
    # Fit functions for interpolation
    def linear_func(x, a, b):
        return a * x + b

    #def log_linear_func(x, a, b):    #Note: Due to it being a log linear function its curve is almost unnoticable due
        #return a*x**2 + b*np.log(x) #the small y-values produced
        #return a*x + b*np.log(x) 

    # Fit the data to the functions
    popt_ls, _ = curve_fit(linear_func, sizes, array_times)  # Linear fit for array times
    popt_bs, _ = curve_fit(linear_func, sizes, linked_list_times)  # Log-linear fit for linked list times

    # Plot the raw timing data
    plt.scatter(sizes, array_times, color='blue', label='Array Data')
    plt.scatter(sizes, linked_list_times, color='red', label='Linked List Data')

    # Plot the fitted curves
    plt.plot(sizes, linear_func(np.array(sizes), *popt_ls), 'b--', label=f"Linear line: {popt_ls[0]:.2e}*n + {popt_ls[1]:.2e}")
    plt.plot(sizes, linear_func(np.array(sizes), *popt_bs), 'r--', label=f"Linear Line: {popt_bs[0]:.2e}*n + {popt_bs[1]:.2e}")

    # Set labels and title
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title("Binary Search Performance: Linked List vs Array")
    plt.show()

measure_performance()
