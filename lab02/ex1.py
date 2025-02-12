import timeit
import matplotlib.pyplot as plt
def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)
'''
1. What does this code do?
 This code is a recursive function that calculates the nth number in a Fibonacci Sequence.
 When n is 0 or 1, it would return 0 or 1 respectively. Else, the function would recursively
 call itself twice. This adds the sum of the 2 numbers before n in the Fibonacci Sequence.'''

'''
2. Is an ecample of a divide-and-conquer-algorithm?
No, this is not an example of a divide-and-conquer algorithm
they are not divided into independent subproblems but rather
overlapping subproblems. Ultimately there is redundancy in the 
sense that the same Fibonacci numbers are recalcualted multiple times.
'''

'''
3. The time complexity is O(2^n). This is a result of the recursive
relation: T(n) = T(n-1) + T(n-2) + O(1). Basically, as n
increases, the alghorithm performs redundant calculations.
The function makes 2 recursive calls for each non-base case and these calls overlap.'''

# 4. 
memo_dict = {}
def func_memo(n):
    # if statement to check of result is already in cache
    if n in memo_dict:
        return memo_dict[n]
    if n <= 1:
        return n
    #cache result
    memo_dict[n] = func_memo(n-1) + func_memo(n-2)
    return memo_dict[n]

'''
5. The complexity is T(n) = O(n). This is because memoization computes each 
Fibonacci number, n,  only once. In addition, the base case and memoization
check are O(1) operations'''

#function to time functions via timeit module
def time(func, max_number):
    #list to store times
    times = []
    #iterate through numbers 0-35, time function execution time for each one,
    # append times to list, return list
    for n in range(max_number + 1):
        elapsed_time = timeit.timeit(lambda: func(n), number=1)
        times.append(elapsed_time)
        print(f'Elapsed time for n={n}: {elapsed_time} seconds')
    return times

max_number = 35
original_times = time(func, max_number)
improved_times = time(func_memo, max_number)
#plot OG function times
plt.figure(figsize=(10,6))

plt.plot(range(max_number + 1), original_times, label="Original", color='red')
plt.title("Execution Time for Original Fib Function")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (sec)")
plt.legend()
plt.savefig("lab02/ex1.6.1.jpg")
plt.show()
#plot improved function times
plt.figure(figsize=(10,6))
plt.plot(range(max_number + 1), improved_times, label="Improved", color='blue')
plt.title("Execution Time for Improved Fib Function")
plt.xlabel("Input Size (n)")
plt.ylabel("Time (sec)")
#adjusted y-axis range as execution times are extremely small for improved func
plt.ylim(0, 0.5)
plt.legend()
plt.savefig("lab02/ex1.6.2.jpg")
plt.show()