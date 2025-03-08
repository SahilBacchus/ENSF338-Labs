import timeit
import random
import matplotlib.pyplot as plt




"""
Answer to question 5: The execution time regarding the linked list
were far longer than the execution time of the array. This is expected
due to the larger amount of time take for linked list to enqueue and
dequeue in comparison to arrays.
"""




class ArrayQueue:
    def __init__(self):
        self.queue = []
   
    def enqueue(self, item):
        self.queue.insert(0, item)
   
    def dequeue(self):
        if self.queue:
            return self.queue.pop()
        return None


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None
   
    def enqueue(self, item):
        new_node = ListNode(item)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
   
    def dequeue(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.value
            self.head = self.tail = None
            return value
        curr = self.head
        while curr.next != self.tail:
            curr = curr.next
        value = self.tail.value
        curr.next = None
        self.tail = curr
        return value


def generate_task_list(size=10000):
    return ["enqueue" if random.random() < 0.7 else "dequeue" for _ in range(size)]


def execute_tasks(queue, tasks):
    for task in tasks:
        if task == "enqueue":
            queue.enqueue(random.randint(1, 100))
        else:
            queue.dequeue()


def measure_performance(queue_class, num_tests=100):
    times = []
    for _ in range(num_tests):
        queue = queue_class()
        tasks = generate_task_list()
        time_taken = timeit.timeit(lambda: execute_tasks(queue, tasks), number=1)
        times.append(time_taken)
    return times


# Measure performance
time_array = measure_performance(ArrayQueue)
time_linked_list = measure_performance(LinkedListQueue)


# Plot results
min_val = min(min(time_array), min(time_linked_list))
max_val = max(max(time_array), max(time_linked_list))
plt.hist(time_array, bins=30, alpha=0.5, label='Array Queue', range=(min_val, max_val))
plt.hist(time_linked_list, bins=30, alpha=0.5, label='Linked List Queue', range=(min_val, max_val))
plt.xlabel("Execution Time (seconds)")
plt.ylabel("Frequency")
plt.title("Performance Comparison of Queue Implementations")
plt.legend()
plt.show()



