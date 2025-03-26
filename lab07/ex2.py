class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # For pivot detection only

class AVL:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        self.root = self._insert(self.root, data)
    
    def _insert(self, node, data):
        if node is None:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        
        # Update height for pivot detection
        node.height = 1 + max(self._get_height(node.left), 
                          self._get_height(node.right))
        
        # Check for pivot and cases
        self._check_cases(node, data)
        
        return node  # No balancing performed
    
    def _get_height(self, node):
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)
    
    def _check_cases(self, node, data):
        balance = self._get_balance(node)
        
        # Case 1: No pivot detected
        if abs(balance) <= 1:
            print("Case #1: Pivot not detected")
            return
        
        # Case 2: Pivot exists and node added to shorter subtree
        if (balance > 1 and data < node.left.data) or (balance < -1 and data > node.right.data):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
            return
        
        # Case 3: All other cases
        print("Case 3 not supported")

# Test Case 1: No pivot (Case 1)
def test_case_1():
    print("\nTest Case 1: Balanced insertions (Case 1)")
    tree = AVL()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    print("Expected: All insertions show Case #1")

# Test Case 2: Pivot exists, added to shorter subtree (Case 2)
def test_case_2():
    print("\nTest Case 2: Creating pivot with shorter subtree addition (Case 2)")
    tree = AVL()
    tree.insert(10)
    tree.insert(5)
    tree.insert(2)  # Creates left-heavy pivot, added to shorter subtree
    print("Expected: Last insertion shows Case #2")

# Test Case 3: Unsupported case (Case 3)
def test_case_3():
    print("\nTest Case 3: Unsupported case (Case 3)")
    tree = AVL()
    tree.insert(10)
    tree.insert(5)
    tree.insert(7)  # Creates left-right imbalance (unsupported case)
    print("Expected: Last insertion shows 'Case 3 not supported'")

# Test Case 4: Right-heavy Case 2
def test_case_4():
    print("\nTest Case 4: Right-heavy Case 2")
    tree = AVL()
    tree.insert(10)
    tree.insert(15)
    tree.insert(20)  # Creates right-heavy pivot, added to shorter subtree
    print("Expected: Last insertion shows Case #2")

if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
