import timeit
import random

"""
Answer to question 4: Binary search is faster than BST search in this case because 
it has an almost guarenteed logarithmetic complexity whereas BST search has an
complexity also logarithmetic but if the tree becomes skewed (unbalanced) enough
its complexity can degrade. In the case that the tree becomes as skewed as it can
possibly become the tree can become a linked list causing the complexity to be linear
instead of logarithmetic. Due to the shuffling of the tree it would be logical to 
assume there was some form of skewing which resulted in the time of the BST search
to increase.

Note: It will not be noticable at a small scale like 10000 elements, for me the 
results became more obvious when I used an array of 1000000 elements for both.
"""

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(root, data):
    if root is None:
        return Node(data)
    
    current = root
    while True:
        if data <= current.data:
            if current.left is None:
                current.left = Node(data, parent=current)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = Node(data, parent=current)
                break
            current = current.right
    
    return root

def build_bst(arr):
    root = None
    for num in arr:
        root = insert(root, num)
    return root

def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_vector = list(range(10000))
shuffled_vector = sorted_vector[:]
random.shuffle(shuffled_vector)

root = build_bst(shuffled_vector)

bst_search_time = timeit.timeit(lambda: [search(num, root) for num in shuffled_vector], number=10)
avg_bst_search_time = bst_search_time / (10 * len(shuffled_vector))

binary_search_time = timeit.timeit(lambda: [binary_search(sorted_vector, num) for num in shuffled_vector], number=10)
avg_binary_search_time = binary_search_time / (10 * len(shuffled_vector))

print(f"BST Search - Total Time: {bst_search_time:.6f}s, Average Time per Element: {avg_bst_search_time:.10f}s")
print(f"Binary Search - Total Time: {binary_search_time:.6f}s, Average Time per Element: {avg_binary_search_time:.10f}s")
