# ########################################################################################
# #-- 1. Implement a class ListPriorityQueue which implements a priority queue using a
# #-- linked list: [0.2 pts]
# #-- • enqueue must insert an element in order
# #-- • dequeue must retrieve the first (smallest) element on a list
# #########################################################################################

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