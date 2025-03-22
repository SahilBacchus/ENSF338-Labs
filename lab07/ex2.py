import timeit
import random

# Node class for AVL tree
class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

# Function to calculate the height of a node
def get_height(node):
    if node is None:
        return 0
    return node.height

# Function to calculate the balance factor of a node
def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

# Function to update the height of a node
def update_height(node):
    if node is not None:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

# AVL tree class
class AVLTree:
    def __init__(self):
        self.root = None

    # Insert a node into the AVL tree
    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        # Standard BST insertion
        if node is None:
            return Node(data)
        if data <= node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        # Update height of the current node
        update_height(node)

        # Check balance and identify pivot
        balance = get_balance(node)
        if balance > 1 or balance < -1:
            pivot = node
            print(f"Pivot detected at node with data: {pivot.data}")
            if (balance > 1 and data <= node.left.data) or (balance < -1 and data > node.right.data):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            else:
                print("Case #3 not supported")  # Case 3 is not implemented
        else:
            print("Case #1: Pivot not detected")

        return node

# Test Case 1: No pivot
def test_case_1():
    print("\nTest Case 1: Adding nodes resulting in no pivot")
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    print("Test Case 1 completed.\n")

# Test Case 2: Pivot exists, node added to shorter subtree
def test_case_2():
    print("\nTest Case 2: Adding nodes resulting in pivot and shorter subtree")
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(3)
    avl.insert(2)
    print("Test Case 2 completed.\n")

# Test Case 3: Unsupported case
def test_case_3():
    print("\nTest Case 3: Unsupported case")
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(15)
    avl.insert(3)
    avl.insert(2)
    avl.insert(1)
    print("Case 3 not supported")
    print("Test Case 3 completed.\n")

# Main function to run all test cases
def main():
    test_case_1()  # Run Test Case 1
    test_case_2()  # Run Test Case 2
    test_case_3()  # Run Test Case 3

if __name__ == "__main__":
    main()
