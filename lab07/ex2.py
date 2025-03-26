class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            return Node(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        # Update height
        node.height = 1 + max(self._get_height(node.left), 
                            self._get_height(node.right))
        
        # Check balance and identify cases
        balance = self._get_balance(node)
        
        # Case 1: No pivot detected
        if abs(balance) <= 1:
            print("Case #1: Pivot not detected")
            return node
        
        # Case 2: Pivot exists, node added to shorter subtree
        if (balance > 1 and data < node.left.data) or (balance < -1 and data > node.right.data):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return node
        
        # Case 3: Not supported
        print("Case 3 not supported")
        return node
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

# Test Case 1: No pivot (Case 1)
def test_case_1():
    print("\nTest Case 1: Adding nodes resulting in no pivot")
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    print("Expected: All insertions should show Case #1")

# Test Case 2: Pivot exists, node added to shorter subtree (Case 2)
def test_case_2():
    print("\nTest Case 2: Adding nodes resulting in pivot and shorter subtree")
    bst = BST()
    bst.insert(10)
    bst.insert(15)
    bst.insert(20)  # Right-heavy, should trigger Case 2
    print("Expected: Last insertion should show Case #2")

# Test Case 3: Unsupported case (Case 3)
def test_case_3():
    print("\nTest Case 3: Adding nodes resulting in unsupported case")
    bst = BST()
    bst.insert(10)
    bst.insert(5)
    bst.insert(7)  # Left-Right imbalance, should trigger Case 3
    print("Expected: Last insertion should show 'Case 3 not supported'")

# Test Case 4: Mixed cases
def test_case_4():
    print("\nTest Case 4: Mixed cases")
    bst = BST()
    bst.insert(10)  # Case 1
    bst.insert(5)   # Case 1
    bst.insert(15)  # Case 1
    bst.insert(3)   # Case 1
    bst.insert(2)   
    bst.insert(4)   
    print("Expected: Should show mix of Case 1, 2, and 3 messages")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
