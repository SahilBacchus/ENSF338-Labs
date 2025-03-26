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




########################################################################
#-- 1. Create a _lr_rotate() method to perform LR rotation [0.3 pts] --#
########################################################################
    def _lr_rotate(self, node):
        left_rotated = self._left_rotate(node.left) # Perform left rotation on the left child
        node.left = left_rotated # Update so that current node left child pointer points to new left rotated sutbtree
        new_root = self._right_rotate(node) # Perform right rotation on current nocde --> makes the grandson the new pivot
        return new_root


##########################################################################
#-- 2. Create a _rl_rotate() method to implement RL rotation [0.3 pts] --#
##########################################################################
    def _rl_rotate(self, node):
        right_rotated = self._right_rotate(node.right) # Perform right rotation on right child
        node.right = right_rotated # Update so that current node left child pointer points to new left rotated sutbtree
        new_root = self._left_rotate(node)  # Perform right rotation on current nocde --> makes the grandson the new pivot
        return new_root

################################################################################
#-- 3. Extend insert() to support case 3b, using the methods above [0.6 pts] --#
################################################################################


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
            if (balance > 1 and data > node.left.data and get_balance(node.left) == 0) or (balance < -1 and data < node.right.data and get_balance(node.right) == 0):
                print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            
            # Case 3A: Left-Left (LL) or Right-Right (RR)
            elif balance > 1 and data < node.left.data:  # LL case
                print("Case #3a: adding a node to an outside subtree")
                return self._right_rotate(node) # perform right rotation
            elif balance < -1 and data > node.right.data:  # RR case
                print("Case #3a: adding a node to an outside subtree")
                return self._left_rotate(node) # perform left rotation
            
            # Case 3B: Left-Right (LR) or Right-Left (RL)
            else:
                if balance > 1:  # left-heavy -> LR rotation
                    print("Case 3b: adding a node to an inside subtree (LR)")
                    return self._lr_rotate(node)
                elif balance < -1:  # right-heavy -> RL rotation
                    print("Case 3b: adding a node to an inside subtree (RL)")
                    return self._rl_rotate(node)
        else:
            print("Case #1: Pivot not detected")

        return node



#################################################################################
#-- 4. Create two extra test cases, both testing case 3b (now the code should --#
#-- not return an error!) [0.3 pts] --------------------------------------------#
#################################################################################


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

# Test Case 3b LR: Left-Right rotation
def test_case_3b_lr():
    print("\nTest Case 3b LR: Adding nodes resulting in a LR rotation")
    avl = AVLTree()
    avl.insert(10)
    avl.insert(5)
    avl.insert(8)  # LR case: 8 inserted in right branch of left child of 10
    print("Test Case 3b LR completed.\n")

# Test Case 3b RL: Right-Left rotation
def test_case_3b_rl():
    print("\nTest Case 3b RL: Adding nodes resulting in a RL rotation")
    avl = AVLTree()
    avl.insert(10)
    avl.insert(15)
    avl.insert(12)  # RL case: 12 inserted in left branch of right child of 10
    print("Test Case 3b RL completed.\n")

# Main function to run all test cases
def main():
    test_case_1()
    test_case_2()
    test_case_3a()
    test_case_3b_lr()
    test_case_3b_rl()

if __name__ == "__main__":
    main()
