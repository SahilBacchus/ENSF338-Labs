import timeit
import matplotlib.pyplot as plt

#######################################################################
#-- 2. Design an optimized implementation of the same function with --#
#-- better performance. Discuss which changes you made and how -------#
#-- they should be expected to result in a better function [0.3 pts --#
#######################################################################

# Impmenting the Singly Linked list as detailed in exercise 7
class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None 

class linked_list:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def insert_head(self, node):
        node.next = self.head
        self.head = node
        self.size += 1 

    def insert_tail(self, node): # no tail ptr so have to traverse the entire list
        if self.head is None: 
            self.head = node
        else: 
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
    
    def get_size(self):
        return self.size

    def get_element_at_pos(self, pos):
        if pos < 0 or pos >= self.size: 
            return None
        current = self.head
        for _ in range(pos):
            current = current.next
        return current 
    
    def reverse_old(self):
        newhead = None
        prevNode = None
        for i in range(self.get_size()-1, -1, -1):
            currNode = self.get_element_at_pos(i)
            currNewNode = Node(currNode.data)
            if newhead is None:
                newhead = currNewNode
            else:
                prevNode.next = currNewNode
            prevNode = currNewNode
        self.head = newhead


    def reverse_new(self): # New implmentation of reverse as described in ex7.md file 
        current = self.head 
        prevNode = None 

        while current is not None:
            nextNode = current.next 
            current.next = prevNode 
            prevNode = current 
            current = nextNode # Traversing the list using the same loop that swaps the elements

        self.head = prevNode


    
    def print_list(self): # Prints the list so we can visually tell if the linked list works
        current = self.head
        while current is not None: 
            print(f"{current.data} -> ", end="")
            current = current.next


# Testing to make sure that our reverse implementation works
llist = linked_list()
llist.insert_head(Node(1))
llist.insert_head(Node(2))
llist.insert_head(Node(3))
llist.insert_head(Node(4))

print("List - no sort\n")
llist.print_list()

print("\nList - new reverse\n")
llist.reverse_new()
llist.print_list()
print("\n-----------------")





##############################################################################
#-- 3. Time both methods (the given one and yours) on list, of 1000, 2000, --#
#-- 3000, 4000 elements, for 100 times. [0.2 pts] ---------------------------#
##############################################################################

def create_linked_list(size):
    llist = linked_list()
    for i in range(size):
        llist.insert_head(Node(i+1))
    return llist


def time_reverse_old(llist): 
    time = timeit.timeit(lambda: llist.reverse_old(), number=100)
    time /= 100
    print(f"reverse_old time for {llist.get_size()}: {time}")
    return time  

def time_reverse_new(llist): 
    time = timeit.timeit(lambda: llist.reverse_new(), number=100)
    time /= 100
    print(f"reverse_new time for {llist.get_size()}: {time}")
    return time 


sizes = [1000, 2000, 3000, 4000]

ro_time = []
rn_time = []


for size in sizes: 
    llist_0 = create_linked_list(size)
    llist_1 = create_linked_list(size)
    ro_time.append(time_reverse_old(llist_0))
    rn_time.append(time_reverse_new(llist_1))






##################################################################################
#-- 4. Plot the measurement results in a X-Y plots for both methods. [0.2 pts] --#
##################################################################################


# Plot the raw timing data
plt.figure(figsize=(10, 6))

plt.scatter(sizes, ro_time, color='blue', label='reverse_old')
plt.scatter(sizes, rn_time, color='red', label='reverse_new')

plt.xlabel('Linked List Size')
plt.ylabel('Time (seconds)')
plt.title('Linked List Reversal: reverse_old vs. reverse_new')
plt.legend()
plt.grid(True)
plt.savefig('lab04/output.7.png')
plt.show()

