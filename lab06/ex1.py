import timeit
import random

"""
Answer to question 4: Creating a non-shuffled tree allowed for a far more balanced tree
which made it faster to traverse through as it was less skewed allowing the search time
to be lower.

"""

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right

def insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    newnode = Node(data, parent)    
    if root is None:
        root = newnode
    elif data <= parent.data:
        parent.left = newnode
    else:
        parent.right = newnode

    return newnode


def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data <= current.data:
            current = current.left
        else:
            current = current.right
    return None

def build_bst_from_sorted_array(arr):
    root = None
    for num in arr:
        root = insert(num, root)
    return root

def measure_search_time(root, arr, trials=10):
    total_time = 0
    for num in arr:
        time_taken = timeit.timeit(lambda: search(num, root), number=trials)
        total_time += time_taken
    avg_time = total_time / len(arr)
    return avg_time, total_time

sorted_array = list(range(10000))

bst_root = build_bst_from_sorted_array(sorted_array)
avg_time_sorted, total_time_sorted = measure_search_time(bst_root, sorted_array)

random.shuffle(sorted_array)

bst_root_shuffled = build_bst_from_sorted_array(sorted_array)
avg_time_shuffled, total_time_shuffled = measure_search_time(bst_root_shuffled, sorted_array)

print(f"Sorted search BST: Avg time = {avg_time_sorted:.10f}, Total time = {total_time_sorted:.5f}")
print(f"Shuffled search BST: Avg time = {avg_time_shuffled:.10f}, Total time = {total_time_shuffled:.5f}")