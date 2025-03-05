## 1. Compare advantages and disadvantages of arrays vs linked list (complexity of task completion) [0.1 pts]

### Arrays 
Advantages: 

- Getting element by index runs in constant time: $O(1)$

Disadvantages: 

- Insertion/Deletion at the head results in the shifting of all elements, making it run in linear time: $O(n)$


### Linked Lists 
Advantages: 

- Insertion at head or tail(assuming you have a tail pointer) takes constant time: $O(1)$

Disadvantages: 

- Getting an element in a list takes linear time, since you have to traverse through the list to find the element: $O(n)$

---

## 2. For arrays, we are interested in implementing a replace function that acts as a deletion followed by insertion. How can this function be implemented to minimize the impact of each of the standalone tasks? [0.1 pts]

This function can be can be optimized by replacing the two operations with one simpler operation of overiting the element at the given index. 

- The old approach would require a deletion and an insertion, due to the need to shift elements, both would have a linear time complexity giving us an overall time complexity of: $O(n)$

- The new approach would find the element by index(takes constant time) and simply overwrite the data that is there resulitng in a time complexity of: $O(1)$

---

## 3. Assuming you are tasked to implement a doubly linked list with a sort function, given the list of sort functions below, state the feasibility of using each one of them and elaborate why is it possible or not to use them. [0.4 pts] 

### 1. Insertion sort

Insertion sort on a doubly linked list is **feasible**. We can achieve this by repeadedly inserting nodes into the sorted portion of the list. By iterating through each node in the unsorted part and inserting it in the correct postion in the sorted portion. 

- To implement this you would need to traverse the sorted portion of the list for each node you want to insert from the unsorted part(needs a nested loop to do), resulting in a time complexity of: $O(n^2)$


### 2. Merge sort

Merge sort on a doubly linked list is **feasible**. We can achieve this similar to merge sort on arrays by continually dividing until we get a sorted sub list. Then we can merge them back by modifying the pointers of the nodes.

- Due to it's divide-and-conquer nature(dividing the list in half is logrithmitc and merging them back is linear) the resulting time complexity is: $O(n*log(n))$


---

## 4. Also show the expected complexity for each and how it differs from applying it to a regular array [0.4 pts]


### Insertion Sort
For a doubly linked list the traversing of the list is more costly requiring O(n) time, whereas in an array shifting the elements is more costly requiring O(n) time 
- Arrays time complexity: $O(n^2)$
- Doubly linked list time complexity: $O(n^2)$

### Merge Sort 
For a doubly linked list the main difference lies in the merging process as it is done with the manipulation of pointers
- Arrays time complexity: $O(n^2)$
- Doubly linked list time complexity: $O(n^2)$
