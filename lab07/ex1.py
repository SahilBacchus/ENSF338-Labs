import timeit
import random

##################################################################################
#-- 1. Implement a binary search tree with insertion and search operations as
#-- seen in class [0.2 pts]
#--     1. It should extend the template provided on D2L with an insert() and a
#--     search() method
###################################################################################

class Node:
    def __init__(self, data, parent=None, left=None, right=None, balance = None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.balance = balance



def findBalance(data):
    return data.parent



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


sorted_array = list(range(10000))

bst_root = build_bst_from_sorted_array(sorted_array)

print(findBalance(bst_root))
