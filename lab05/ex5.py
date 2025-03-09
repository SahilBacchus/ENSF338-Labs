# Exercise 5

# 5.1
class ArrayCircularQueue:
    def __init__(self, size):
        self.size = size # set max size of queue
        self.queue = [None] * size # initialize queue with none values
        self.head = -1 # index of head element
        self.tail = -1 # index of tail element
    
    def enqueue(self, element):
        # check if queue is full
        # ex: 4 % 4 = 0 = head meaning its full
        if (self.tail + 1) % self.size == self.head:
            print("enqueue None")
            return
        # if queue is empty
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.size # move tail pointer circularly (ex: 3 + 1 = 4 % 5 = 4)
        self.queue[self.tail] = element #insert element at tail pos
        print(f"enqueue {element}") # print the enqueue op

    def dequeue(self):
        # if queue is empty
        if self.head == -1:
            print("dequeue None")
            return None
        # store head element in temp variable
        temp = self.queue[self.head]
        # if only 1 element in queue, set head and tail to -1 (to indicate empty)
        if self.head == self.tail:
            self.head = self.tail = -1
        else: # increment head pointer
            self.head = (self.head + 1) % self.size
        print(f"dequeue {temp}")
        return temp
    
    def peek(self):
        # if queue is empty
        if self.head == -1:
            print("dequeue None")
            return None
        temp = self.queue[self.head]
        print(f"peek {temp}")  
        return temp

# 5.2              
class Node:
    def __init__(self, value):
        # intialize value and next pointer in Node class
        self.value = value
        self.next = None

class LinkedListCircularQueue:
    def __init__(self, size):
        self.size = size #  not necessary to maintain size in linked list, but makes it easier for checking if queue is full/empty
        self.head = None # head pointer
        self.tail = None # tail pointer
        self.count = 0 # tracks number of elements in queue

    def enqueue(self, element):
        # check if queue is full
        if self.count == self.size:
            print("enqueue None")
            return
        new_node = Node(element)
        # checks if queue is empty
        if not self.head:
            self.head = self.tail  = new_node # set head and tail ptr to new_node
            self.tail.next = self.head # set tail next ptr to head to make it circular
        else:
            self.tail.next = new_node # insert new node to end
            self.tail = new_node # update tail pointer to point to new node
            self.tail.next = self.head # keep circlar link
        self.count += 1 # increase element count
        print(f"enqueue {element}")

    def dequeue(self):
        # check of queue is empty
        if self.count == 0:
            print("dequeue None")
            return None
        temp = self.head.value # get first element in queue
        # check if queue becomes empty after dequeue
        if self.head == self.tail:
            self.head = self.tail = None
        else: # move head pointer and adjust tail ptr
            self.head = self.head.next
            self.tail.next = self.head
        self.count -= 1 # decrease element count
        print(f"dequeue {temp}")
        return temp

    def peek(self):
    # check of queue is empty
        if self.count == 0:
            print("dequeue None")
            return None
        temp = self.head.value
        print(f"peek {temp}")
        return temp


# 5.3
# Test case list with 40 operations
def test_circular_queue(queue):
    operations = [
        (queue.enqueue, 1), (queue.enqueue, 2), (queue.enqueue, 3),  # Enqueue elements
        (queue.peek, None), (queue.dequeue, None), (queue.peek, None),  # Peek and dequeue operations
        (queue.enqueue, 4), (queue.enqueue, 5), (queue.enqueue, 6),  # Enqueue until full
        (queue.enqueue, 7), (queue.dequeue, None), (queue.dequeue, None),  # Dequeue operations
        (queue.enqueue, 8), (queue.enqueue, 9), (queue.enqueue, 10),  # More enqueue operations
        (queue.dequeue, None), (queue.dequeue, None), (queue.peek, None),  # Peek and dequeue
        (queue.dequeue, None), (queue.dequeue, None), (queue.dequeue, None),  # Emptying queue
        (queue.dequeue, None), (queue.dequeue, None), (queue.dequeue, None),  # Additional dequeue operations on empty queue
        (queue.enqueue, 11), (queue.enqueue, 12), (queue.enqueue, 13),  # Enqueue new elements
        (queue.enqueue, 14), (queue.enqueue, 15), (queue.enqueue, 16),  # Fill up the queue
        (queue.enqueue, 17), (queue.enqueue, 18), (queue.enqueue, 19),  # Continue enqueueing
        (queue.enqueue, 20), (queue.peek, None), (queue.dequeue, None),  # Peek and dequeue
        (queue.enqueue, 21), (queue.enqueue, 22), (queue.enqueue, 23),  # Enqueue additional elements
        (queue.peek, None), (queue.dequeue, None)  # Final peek and dequeue
    ]
    
    for op, arg in operations:
        if arg is not None:
            op(arg)  # Call the operation with argument
        else:
            op()  # Call the operation without argument

# Example usage
print("Testing ArrayCircularQueue")
queue1 = ArrayCircularQueue(5)  # Create a queue with size 5
test_circular_queue(queue1)  # Run the test cases

print("\nTesting LinkedListCircularQueue")
queue2 = LinkedListCircularQueue(5)  # Create a queue with size 5
test_circular_queue(queue2)  # Run the test cases

