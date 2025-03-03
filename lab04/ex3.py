import sys
import timeit
import matplotlib.pyplot as plt
import numpy as np

"""
1.Identify and explain the strategy used to grow arrays when full, with
references to specific lines of code in the file above. What is the
growth factor?


Answer: Whenever the array is full it reallocates the array along with 
more memory then required in order to make the reallocation of arrays
infrequent. This resize can be seen through line 44 of list.c which
is the function list_resize. The first if statement of the function 
(line 54) checks to see if there is in fact space in the array in order 
to bypass reallocation of the array. However, once it has confirmed the 
array has no space it starts the reallocation process. The growth factor
of the array is in line 70 where it allocates 1/8 more than the 
original arrays size. This is done through the bitwise operator (>>)
which shifts bits to the right 3 times resulting in a division by 8.
It also adds a constant value of 6 to ensure that the array is growing.
Once the adding is done it is formatted to be divisible by 4. This is 
done by using the AND operator to with the NOT of 3. Resulting in the
last two binary digits to always be zero creating a multiple of 4. 
Finally meaning that it creates a growth factor of 1.125.



5.Plot the distribution of both measurements (you can use hist or
similar). Do you see any difference? Why?


Answer: The difference is visible, though not extreme. I presume the 
reason for this is because of the use of very small arrays. The plot 
shows that when resizing S to S+1 is slower than resizing S to S-1.
The reason for this is because when you resize S to S+1 the array 
needs to be reallocated with an increased memory. Causing a time
complexity of O(n). Whereas when deleting an element resizing 
isn't required.

"""


# Question 2: Track capacity changes
def track_list_growth():
    lst = []
    list_size = sys.getsizeof(lst)
    prev_capacity = 0
    print("Capacity\tElement Capacity")
    for i in range(64):
        lst.append(i)
        new_capacity = (sys.getsizeof(lst) - list_size)#Convert bytes to elements
        if new_capacity != prev_capacity:
            print(f"{new_capacity} bytes\t{(int) (new_capacity/4)} elements")
            prev_capacity = new_capacity

track_list_growth()

# Find the largest S that triggers a resize
lst = []
last_capacity = sys.getsizeof(lst)
S = 0
for i in range(1000):
    lst.append(i)
    new_capacity = sys.getsizeof(lst)
    if new_capacity != last_capacity:
        last_capacity = new_capacity
        S = i  # This is the value that triggers a resize

# Question 3 & 4: Measure growth times
def measure_time_growth(S, repetitions=1000):
    lst = list(range(S))
    return timeit.timeit(lambda: (lst.append(S), lst.pop()), number=repetitions) / repetitions

times_S_to_S1 = [measure_time_growth(S) for _ in range(1000)]
times_Sm1_to_S = [measure_time_growth(S-1) for _ in range(1000)]

# Question 5: Plot distributions
plt.hist(times_S_to_S1, bins=50, alpha=0.5, label='S → S+1')
plt.hist(times_Sm1_to_S, bins=50, alpha=0.5, label='S → S-1')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Growth Time Distributions')
#plt.savefig("output.png")
plt.show()
