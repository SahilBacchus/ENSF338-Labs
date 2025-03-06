# import appropriate modules
import random
import timeit
import matplotlib.pyplot as plt
import array

# 1. implemented a stack which uses Pythom arrays
class ArrayStack:
    def __init__(self):
        # initialize signed integer array to stack attribute
        self.stack = array.array('i')

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        # checks if stack is empty or not
        if self.stack:
            return self.stack.pop()
        # returns none if stack is empty
        return None
    
# 2. implemented a linked list which uses a singly-linked list
# Node class for LinkedListStack class to use 
class Node:
    def __init__(self, value):
        # intialize value and next pointer in Node class
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, item):
        # insert element at the head of the list
        new_node = Node(item)
        # newly inserted node's next ptr points to where
        # head pointer currently points to
        new_node.next = self.head
        # head pointer now points to new node inserted
        self.head = new_node

    def pop(self):
        # if linkedlist is not empty:
        if self.head:
            # copy the element at the head of the list
            value = self.head.value
            # have the head pointer point to the second element 
            # as the first element is going to be deleted
            self.head= self.head.next
            # return the element
            return value
            # the node will be auto deleted bc of Python's GC
        return None
# 3. function that generates random lists of 10000 tasks
def generate_tasks(n):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            tasks.append(('push', random.randint(1, 100)))
        else:
            tasks.append(('pop', None))
    return tasks
    
def execute_tasks(stack, tasks):
    for operation, value in tasks:
        if operation == 'push':
            stack.push(value)
        else:
            stack.pop()
# 4. function that measures the performance
def measure_performance(stack_class, task_lists):
    times = []
    print(f"\nExecution Times for {stack_class.__name__} (seconds):")

    for tasks in task_lists:
        stack = stack_class()
        elapsed_time = timeit.timeit(lambda: execute_tasks(stack, tasks), number=1)
        times.append(elapsed_time)
        print(f"{elapsed_time:.6f} sec")
    return times
    
task_lists = [generate_tasks(10000) for _ in range(100)]
    
array_stack_times = measure_performance(ArrayStack, task_lists)
linked_list_stack_times = measure_performance(LinkedListStack, task_lists)


 # 5. Plot results
plt.figure(figsize=(10, 6))
plt.hist(array_stack_times, bins=20, alpha=0.5, label='Array Stack', color='blue')
plt.hist(linked_list_stack_times, bins=20, alpha=0.5, label='Linked List Stack', color='red')
plt.xlabel('Execution Time (seconds)')
plt.ylabel('Frequency')
plt.title('Performance Comparison of Stack Implementations')
plt.legend()
plt.show()

# results discussion:
# From the histograms, it appears the array-based stack is generally faster 
# in execution time than the linked list-based stack with their frequencies
# taken into account as well. The reason why the array-based stack is slightly
# faster because linked-lists have added overhead of pointer storage and is 
# usually slower as a result of more complex memory access patterns. Also, 
# array-based stacks have better cache locality as their elements are stored
# in contiguous blocks of memory.