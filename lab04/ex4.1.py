# Exercise 4
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2


'''
1. 
Best-Case: The best case happens when no elements in the array
li satisfy li[i] > 5. Because of this, the inner loop would never
execute, and the function would only iterate through the outer 
loop n times. So, the time complexity is O(n).

Worst-Case: The worse case happens when every elemeny in the array 
li satifies li[i] > 5. This means that for every iteration of the
outer loop, the inner loop executes. The outer loop runs n times
and the inner loop runs n times for every iteration of the outer loop.
So, this means the time complexity is O(n) x O(n) = O(n x n) = O(n^2).

Average-Case: The average case occurs when around half of the elements in
the array li satisfy the condition li > 5. This means the inner loop
runs approximately n/2 times and the outer loop runs n times. Because constants 
are ignored in Big-O notation, the time complexity is O(n/2) x O(n) 
= O((n/2) x n) = O(n^2/2) = O(n^2).
'''

# 2. 
# No, only the worst case and average case are the same, not all three.
# Modified version of code so best, worse, and average case complexities
# are the same:

def processdatamod(li):
    for i in range(len(li)):
        for j in range(len(li)):
            li[i] *= 2

# In this implementation, we remove the conditional statement li[i] > 5 entirely.
# This ensures the inner loop always runs n times for every iteration of the outer loop.
# The outer loop runs n times per usual.
# So, the time complexities for all cases would be O(n) x O(n) = O(n x n) = O(n^2).