import random
import timeit


########################################################################################
#-- 1. Implement a class ListPriorityQueue which implements a priority queue using a --#
#-- linked list: [0.2 pts] ------------------------------------------------------------#
#-- • enqueue must insert an element in order -----------------------------------------#
#-- • dequeue must retrieve the first (smallest) element on a list --------------------#
#########################################################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LListPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        new_node = Node(data)
        
        if self.head is None or self.head.value > data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.value <= data:
                current = current.next
            
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.head is None:
            return None
        
        value = self.head.value
        self.head = self.head.next

        return value
    
    def print_queue(self):
        current = self.head
        while current is not None:
            print(f"{current.value} -->", end=" ")
            current = current.next
        print("None")  # This shows the end of the queue



pq = LListPriorityQueue()
pq.enqueue(4)
pq.enqueue(2)
pq.enqueue(5)
pq.enqueue(3)
pq.enqueue(1)

print("-----------------------")
print("Testing LListPriorityQueue")
pq.print_queue()
print(f"Dequeuing: {pq.dequeue()}")
pq.print_queue()
print("-----------------------")




######################################################################################
#-- 2. Implement a class HeapPriorityQueue which implements a priority queue using --#
#-- a heap: [0.2 pts] ---------------------------------------------------------------#
######################################################################################

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, val):
        self.heap.append(val) 
        self.bubble_up(len(self.heap) - 1)
    
    def dequeue(self):
        if not self.heap:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop() 
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.bubble_down(0)
        return root
    
    def bubble_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent  
            parent = (index - 1) // 2  
    
    def bubble_down(self, index):
        left_child = 2 * index + 1  
        right_child = 2 * index + 2  
        smallest = index 
        
        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child
        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.bubble_down(smallest)  

    def print_queue(self):
        print(self.heap)



pq = HeapPriorityQueue()
pq.enqueue(4)
pq.enqueue(2)
pq.enqueue(5)
pq.enqueue(3)
pq.enqueue(1)

print("-----------------------")
print("Testing HeapPriorityQueue")
pq.print_queue()
print(f"Dequeuing: {pq.dequeue()}")
pq.print_queue()
print("-----------------------")


######################################################################################
#-- 3. Measure execution time of both implementations [0.4 pts] ---------------------#
######################################################################################


def generate_tasks(num_tasks=1000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:  # 70% chance for enqueue
            tasks.append('enqueue')
        else:  # 30% chance for dequeue
            tasks.append('dequeue')
    return tasks

def simulate_priority_queue(tasks, pq):
    for task in tasks:
        if task == 'enqueue':
            pq.enqueue(random.randint(1, 100))
        elif task == 'dequeue':
            pq.dequeue()

def time_priority_queue(tasks, pq):
    return timeit.timeit(lambda: simulate_priority_queue(tasks, pq), number=1)



num_tasks = 1000
tasks = generate_tasks(num_tasks)

llistpq = LListPriorityQueue()
heappq = HeapPriorityQueue()

llistpq_total_time = time_priority_queue(tasks, llistpq)
llistpq_avg_time = llistpq_total_time /  len(tasks)
heappq_total_time = time_priority_queue(tasks, heappq)
heappq_avg_time = heappq_total_time / len(tasks)




print("\n\n-----------------------")
print(f"Times for for {num_tasks} tasks")
print(f"LListPriorityQueue avg. task time: {llistpq_avg_time:.6e} seconds")
print(f"HeapPriorityQueue avg. task time: {heappq_avg_time:.6e} seconds")
print(f"\nLListPriorityQueue total time: {llistpq_total_time:.8f} seconds")
print(f"HeapPriorityQueue total time: {heappq_total_time:.8f} seconds")
print("-----------------------")



#########################################################################################
#-- 4. Discuss the results: which implementation is faster? Why do you think is that? --#
#-- [0.2 pts] --------------------------------------------------------------------------#
#########################################################################################

'''
-----------------------
Times for for 1000 tasks
LListPriorityQueue avg. task time: 5.110600e-06 seconds 
HeapPriorityQueue avg. task time: 3.689200e-06 seconds  

LListPriorityQueue total time: 0.00511060 seconds       
HeapPriorityQueue total time: 0.00368920 seconds        
-----------------------


Discuss:
From these results we notice that the HeapPriorityQueue is FASTER than LListPriorityQueue. 


LListPriorityQueue 
    enqueue:
        - This operation due to having to at worst traverse the whole list 
        to find the correct insertion spot has a time complexity of O(n) 
    dequeue:
        - This operation due to us popping at the head  has 
        a time complexity of O(1)

HeapPriorityQueue
    enqueue:
        - This operation has a time complexity of O(log(n)) 
    dequeue:
        - This operation has a time complexity of O(log(n))


Due to our simulation mostly testing enqueue of which HeapPriorityQueue is faster(since O(log(n)) < O(n)), 
this results in HeapPriorityQueue being faster overall in our simulation even though LListPriorityQueue has a 
faster dequeue. 



'''
