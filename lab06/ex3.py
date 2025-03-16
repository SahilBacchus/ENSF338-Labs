import sys
# Binary Tree Node that holds value and pointers to right and left child
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# this function parses the expression into a binary tree
def parse_expression(tokens):
   
    def parse():
        # retrieve the first token and remove it from the list
        token = tokens.pop(0)

        if token == '(': # if first token is (, parse the sub expression)
            left = parse() # parse left subtree recursively
            operator = tokens.pop(0) # retrieve operator
            right = parse() # parse right subtree recursively
            tokens.pop(0)  # remove the closing ')'
            return Node(operator, left, right) # return a new Node with the operator and operands
        else:
            try:
                return Node(float(token))  # Convert numbers correctly
            except ValueError:
                # if not a number, store as an operator node
                return Node(token)

    return parse()

# function that evaluates binary tree via post-order traversal
def evaluate_postorder(node):
    # checks if node is empty
    if node is None:
        return 0

    if isinstance(node.value, float):  # If it's a number, return it
        return node.value

    # evaluate left subtree recursively first
    left_value = evaluate_postorder(node.left)
    # then evaluate right subtree recursively
    right_value = evaluate_postorder(node.right)

    # conditions to check node's operator and perform op
    if node.value == '+':
        return left_value + right_value
    elif node.value == '-':
        return left_value - right_value
    elif node.value == '*':
        return left_value * right_value
    elif node.value == '/':
        return left_value / right_value
    else:
        # error handling for invalid op
        raise ValueError(f"Unknown operator: {node.value}")

def main():
    # check if user has provided exactly 1 argument
    # the other argument is the scriptname automatically provided
    # that's why we use 2
    if len(sys.argv) != 2:
        print("Usage: python ex3.py \"expression\"")
        return
    
    # store users input into expression variable
    expression = sys.argv[1]
    
    # Tokenize the expression correctly via adding spaces around parentheses before splitting
    tokens = expression.replace("(", " ( ").replace(")", " ) ").split()
    
    # Parse the expression into a binary tree
    root = parse_expression(tokens)
    
    # Compute the result using post-order traversal
    result = evaluate_postorder(root)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
