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

    # function that performs left rotation on given node
    def _left_rotate(self, node):
        new_root = node.right # the new root is the right child
        node.right = new_root.left # Move the left child of the new root to the right of the old root
        new_root.left = node  # Make the old root the left child of the new root
        update_height(node) # update height of the old root
        update_height(new_root) # update height of the new root
        return new_root # return new root

    # function that performs right rotation on given node
    def _right_rotate(self, node):
        new_root = node.left # the new root is tne left child
        node.left = new_root.right  # Move the right child of the new root to the left of the old root
        new_root.right = node # Make the old root the right child of the new root
        update_height(node) # update height of old root
        update_height(new_root) # update new root height
        return new_root # return new root

    # Insert a node into the AVL tree
    def insert(self, data):
        self.root = self._insert(self.root, data)

    # Standard BST insertion
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        # Update height of the current node
        update_height(node)
        # cehck balance factor
        balance = get_balance(node)

        # If the node becomes unbalanced, determine the case
        if balance > 1 or balance < -1:
            pivot = node
            print(f"Pivot detected at node with data: {pivot.data}")
            
            # Case 2: A pivot exists, and a node was added to the shorter subtree
            if (balance > 1 and data > node.left.data) or (balance < -1 and data < node.right.data):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            
            # Case 3A: Left-Left (LL) or Right-Right (RR)
            elif balance > 1 and data < node.left.data:  # LL case
                print("Case #3a: adding a node to an outside subtree")
                return self._right_rotate(node) # perform right rotation
            elif balance < -1 and data > node.right.data:  # RR case
                print("Case #3a: adding a node to an outside subtree")
                return self._left_rotate(node) # perform left rotation
            else:
                # Case 3B: Left-Right (LR) or Right-Left (RL) (not supported)
                print("Case 3b not supported")
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

# Test Case 3a: Case 3a
def test_case_3a():
    print("\nTest Case 3a: Adding nodes resulting in Case 3a (LL or RR)")
    avl = AVLTree()
    avl.insert(30)
    avl.insert(20)
    avl.insert(10)  # LL case triggers rotation
    print("Test Case 3a completed.\n")

# Test Case 3b: Case 3b unsupported
def test_case_3b():
    print("Test Case 3b not supported")
    #print("\nTest Case 3b: Adding nodes resulting in Case 3b (LR or RL)")
    #avl = AVLTree()
    #avl.insert(10)
    #avl.insert(5)
    #avl.insert(8)  # LR case (unsupported)
    #print("Test Case 3b completed.\n")

# Main function to run all test cases
def main():
    test_case_1()
    test_case_2()
    test_case_3a()
    test_case_3b()

if __name__ == "__main__":
    main()