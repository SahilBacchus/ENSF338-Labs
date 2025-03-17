import random
import unittest

class Heap:
    def __init__(self):
        # initialize empty list to store heap elements
        self.heap = []
    
    def heapify(self, arr):
        # transform list into proper min-heap
        self.heap = arr[:]
        # len*self.heap) // 2 gives index of the first leaf node
        # then - 1 gives the index of the last non-leaf node
        # start heapiyfing from last non-leaf node
        for i in range(len(self.heap) // 2 - 1, -1, -1):  # Start from the last non-leaf node
            self.bubble_down(i)
    
    def enqueue(self, val):
        self.heap.append(val)  # Add the element at the end
        self.bubble_up(len(self.heap) - 1)  # Move it up to maintain heap order
    
    def dequeue(self):
        # check if heap is empty
        if not self.heap:
            return None  # Return None if heap is empty
        # check for case only 1 element in array
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, pop and return it
        root = self.heap[0]  # Get the root element (smallest element)
        self.heap[0] = self.heap.pop()  # Move the last element to the root
        self.bubble_down(0)  # Restore heap property
        return root
    
    def bubble_up(self, index):
        parent = (index - 1) // 2  # Get the parent index
        while index > 0 and self.heap[index] < self.heap[parent]:  # If the element is smaller than its parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]  # Swap them
            index = parent  # Move up to the parent index
            parent = (index - 1) // 2  # Recalculate parent index
    
    def bubble_down(self, index):
        left_child = 2 * index + 1  # Left child index
        right_child = 2 * index + 2  # Right child index
        smallest = index  # Assume the current index is the smallest
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child  # Update smallest index if left child is smaller
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child  # Update smallest index if right child is smaller
        if smallest != index:  # If the smallest index is not the current index
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]  # Swap
            self.bubble_down(smallest)  # Recursively bubble down

class TestHeap(unittest.TestCase):
    def test_already_heapified(self):
        # test with valid heap
        arr = [1, 3, 5, 7, 9, 11]
        heap = Heap()
        heap.heapify(arr)
        self.assertEqual(heap.heap, [1, 3, 5, 7, 9, 11])  # Should remain the same
    
    def test_empty_heap(self):
        # test with empty arr
        arr = []
        heap = Heap()
        heap.heapify(arr)
        self.assertEqual(heap.heap, [])  # Should remain empty
    
    def test_random_list(self):
        # test with random integers
        # Random order list from 1 to 100
        arr = random.sample(range(1, 101), 100)  
        heap = Heap()
        heap.heapify(arr)
        expected = sorted(arr)  # A valid min-heap is sorted in level order (expected result)
        
        for i in range(len(expected) // 2):  # Ensure heap property is maintained
            # calculate positions of left and right child
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < len(expected):
                self.assertLessEqual(expected[i], expected[left_child])
            if right_child < len(expected):
                self.assertLessEqual(expected[i], expected[right_child])
        
if __name__ == "__main__":
    unittest.main()
