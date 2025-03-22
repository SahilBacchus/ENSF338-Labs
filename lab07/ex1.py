import timeit
import random
import matplotlib.pyplot as plt

##################################################################################
#-- 1. Implement a binary search tree with insertion and search operations as
#-- seen in class [0.2 pts]
#--     1. It should extend the template provided on D2L with an insert() and a
#--     search() method
###################################################################################

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

# Insert a node into the BST
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

    # Update heights and balance factors for all ancestors
    current = newnode
    while current is not None:
        update_height(current)
        current = current.parent

    return newnode

# Search for a node in the BST
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

# Function to measure the balance of the entire tree
def measure_balance(root):
    balances = []
    _measure_balance(root, balances)
    return balances

def _measure_balance(node, balances):
    if node is not None:
        balance = get_balance(node)
        balances.append(abs(balance))
        _measure_balance(node.left, balances)
        _measure_balance(node.right, balances)

# Function to generate 1000 random search tasks
def generate_search_tasks():
    numbers = list(range(1, 1001))
    tasks = []
    for _ in range(1000):
        random.shuffle(numbers)
        tasks.append(numbers.copy())
    return tasks

# Function to measure average search time and largest absolute balance
def measure_performance(root, tasks):
    search_times = []
    largest_balances = []

    for task in tasks:
        start_time = timeit.default_timer()
        for number in task:
            search(number, root)
        end_time = timeit.default_timer()

        avg_search_time = (end_time - start_time) / 1000
        search_times.append(avg_search_time)

        largest_balance = max(measure_balance(root))
        largest_balances.append(largest_balance)

    return search_times, largest_balances

# Function to plot the scatterplot
def plot_scatter(balances, search_times):
    plt.scatter(balances, search_times, alpha=0.5)
    plt.xlabel("Largest Absolute Balance")
    plt.ylabel("Average Search Time (seconds)")
    plt.title("BST Performance vs Balance")
    plt.show()

# Main function for Exercise #1
def main():
    # Create a BST and insert random data
    root = None
    for _ in range(1000):
        root = insert(random.randint(1, 1000), root)

    # Generate search tasks
    tasks = generate_search_tasks()

    # Measure performance
    search_times, largest_balances = measure_performance(root, tasks)

    # Plot results
    plot_scatter(largest_balances, search_times)

if __name__ == "__main__":
    main()
