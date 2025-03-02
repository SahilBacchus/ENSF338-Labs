import time
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d as inter

""" 
Answer to Question 4: Binary Search for a Linked List unlike an array,
requires to first go "travel" through the list in order to find the
mid point. This causes a time complexity of O(n) prior to even doing
the search as you have to search for the mid point in order to use
binary search. In my opinion it is almost like using linear search
to search for the midpoint in order to use binary search. Therefore, 
to me it's logical to conclude that the time complexity of binary 
search on a linked list is O(nlog(n)).
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
        
        start = time.time()
        linked_list.binary_search(target)
        linked_list_times.append(time.time() - start)
        
        start = time.time()
        array.binary_search(target)
        array_times.append(time.time() - start)
    
    x_new = np.linspace(min(sizes), max(sizes), 300)
    linked_list_interp = inter(sizes, linked_list_times, kind='quadratic')
    array_interp = inter(sizes, array_times, kind='linear')
    
    plt.plot(sizes, linked_list_times, 'o')
    plt.plot(sizes, array_times, 'o')
    plt.plot(x_new, linked_list_interp(x_new), '-', label="Linked List (Interpolated)")
    plt.plot(x_new, array_interp(x_new), '-', label="Array (Interpolated)")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.title("Binary Search Performance: Linked List vs Array")
    plt.show()

measure_performance()