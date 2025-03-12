import random 
import timeit
import matplotlib.pyplot as plt


###############################################################################
#-- 1. Implement a priority queue class based on Python arrays (ref. to the --#
#-- discussion in the lecture on queues) [0.3 pts] ---------------------------#
###############################################################################

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = arr[low: mid + 1]
    right = arr[mid + 1: high + 1]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1




class PriorityQueue1: 
    def __init__(self):
        self.queue = [] 

    def enqueue(self, data):
        self.queue.append(data)
        merge_sort(self.queue, 0, len(self.queue)-1)

    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def print_queue(self):
        print(self.queue)



# Test if PriorityQueue1 is working properly 
pq1 = PriorityQueue1()
pq1.enqueue(4)
pq1.enqueue(2)
pq1.enqueue(5)
pq1.enqueue(3)
pq1.enqueue(1)

print("-----------------------")
print(f"Testing PriorityQueue1")
pq1.print_queue()
print(f"dequeing: {pq1.dequeue()}")  # Output: 2
pq1.print_queue()  
print("-----------------------")





###########################################################
#-- 2. Implement another priority queue class [0.3 pts] --#
###########################################################

class PriorityQueue2: 
    def __init__(self):
        self.queue = [] 

    def enqueue(self, data):
        for i in range(len(self.queue)):
            if self.queue[i] > data:
                self.queue.insert(i, data)
                return 
        self.queue.append(data)


    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def print_queue(self):
        print(self.queue)


# Test if PriorityQueue2 is working properly 
pq2 = PriorityQueue2()
pq2.enqueue(4)
pq2.enqueue(2)
pq2.enqueue(5)
pq2.enqueue(3)
pq2.enqueue(1)

print("-----------------------")
print(f"Testing PriorityQueue2")
pq2.print_queue()
print(f"dequeing: {pq2.dequeue()}")  # Output: 2
pq2.print_queue()  
print("-----------------------")




############################################################################
#-- 3. Write a function which generates random lists of 1000 tasks. Each --#
#-- task is either an enqueue w/ probability 0.7, or a dequeue w/ ---------#
#-- probability 0.3 [0.3 pts] ---------------------------------------------#
############################################################################

def generate_tasks(num_tasks=1000):
    tasks = []
    for _ in range(num_tasks):
        if random.random() < 0.7:  # 70% chance for enqueue
            tasks.append('enqueue')
        else:  # 30% chance for dequeue
            tasks.append('dequeue')
    return tasks


######################################################################
#-- 4. Measure the performance of both implementations on 100 such --#
#-- lists using timeit and print the results [0.3 pts] --------------#
######################################################################

def simulate_priority_queue(tasks, pq):
    for task in tasks:
        if task == 'enqueue':
            pq.enqueue(random.randint(1, 100))
        elif task == 'dequeue':
            pq.dequeue()

def time_priority_queue(tasks, pq):
    return timeit.timeit(lambda: simulate_priority_queue(tasks, pq), number=1)


num_tasks = 1000
pq1_times = []
pq2_times = []

for _ in range(100):
    tasks =  generate_tasks(num_tasks)
    pq1 = PriorityQueue1()
    pq2 = PriorityQueue2()

    pq1_times.append(time_priority_queue(tasks, pq1))
    pq2_times.append(time_priority_queue(tasks, pq2))


pq1_total_time = sum(pq1_times)
pq2_total_time = sum(pq2_times)
pq1_avg_time = pq1_total_time / len(pq1_times)
pq2_avg_time = pq2_total_time / len(pq2_times)


print("\n\n-----------------------")
print(f"Times for for {num_tasks} tasks")
print(f"PriorityQueue1 avg. time: {pq1_avg_time:.6f} seconds")
print(f"PriorityQueue2 avg. time: {pq2_avg_time:.6f} seconds")
print(f"\nPriorityQueue1 total time(for 100 iterations): {pq1_total_time:.6f} seconds")
print(f"PriorityQueue2 total time(for 100 iterations): {pq2_total_time:.6f} seconds")
print("-----------------------")









##############################################################################
#-- 5. Discuss the results: which implementation is faster? Why? [0.3 pts] --#
##############################################################################

'''
From Output: 
-----------------------
Times for for 1000 tasks
PriorityQueue1 avg. time: 0.109945 seconds
PriorityQueue2 avg. time: 0.001158 seconds

PriorityQueue1 total time(for 100 iterations): 10.994527 seconds      
PriorityQueue2 total time(for 100 iterations): 0.115808 seconds       
-----------------------


Discuss:
From these results we notice that the PriorityQueue2 is FASTER than PriorityQueue1. 
This discrepency is due to the slower performance of having to do mergesort for each 
enqueue for PriorityQueue2. 


ProirityQueue1 (pq1)
    enqueue:
        - This operation due to having to perform merge sort 
        has a time complexity of O(n*log(n)) 
    dequeue:
        - This operation due to us popping at beginning of array has 
        a time complexity of O(n)

ProirityQueue2 (pq2)
    enqueue:
        - This operation due to linearly searching to find where to put element 
          has a time complexity of O(n) 
    dequeue:
        - This operation due to us popping at beginning of array has 
        a time complexity of O(n)


Both have the same dequeue time complexity, however for enqueue pq1 has a time complexity of 
O(n*log(n))  which is greater than the O(n) time complexity that pq2 has. Meaning overall pq2 
is faster than pq1 especially since our tests are baised towards enqueue operations. 



'''