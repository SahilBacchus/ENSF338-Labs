## 1. Give an expression for the time complexity of the reverse()implementation. Explain how you reached the conclusion describing your step-by-step reasoning. [0.3 pts]

The time complexity of the reverse() implementation would be $O(n^2)$

This is due there being a nested for loop as presumbly the self.get_element_at_pos(i) would loop through the entire array to find the element at position i. 

- Overall time complexity: n*n steps(nested loops) = $O(n^2)$



---


## 2. Design an optimized implementation of the same function with better performance. Discuss which changes you made and how they should be expected to result in a better function [0.3 pts]

We could optimize the reverse() function by taking out the get_element_at_pos(i) and instead increment the head pointer to traverse the list as we are already in the same loop that would handle the actual reversing of elements part.

The aformentioned changes will result in a reduction in time complexity(since we now only use one loop instead of two)

- New time complexity: $O(n)$