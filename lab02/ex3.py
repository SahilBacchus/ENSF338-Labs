#########################################################################################################
#----- 1) What is a profiler, and what does it do? [0.25 pts] ------------------------------------------#
#########################################################################################################
'''
A profiler is a tool that uses various techniques to  analyze a functions runtime behavior.
    - ex) how long functions are called, how much memory it takes, etc. 
'''

#########################################################################################################
#-----2) How does profiling differs from benchmarking? [0.25 pts] --------------------------------------#
#########################################################################################################
'''
Profiling helps us understand the behaviour of individual code segments, allowing us to 
pinpoint where potential performance bottlenecks could be. 

        VS

Benchmarking which aims to measure overall performance over standardized tests, giving us
a way to compare programs but not offering insights on where to improve the code like
profiling offers. 
'''

#########################################################################################################
#-----3) Use a profiler to measure execution time of the program (skipfunction definitions) [0.25 pt] --#
#########################################################################################################
import timeit
import cProfile
import re

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)


def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data


def third_function():
# third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]



# Segment of code to profile
pr = cProfile.Profile()

pr.enable()
test_function()
third_function()
pr.disable()

pr.print_stats()



#########################################################################################################
#-----4) Discuss a sample output. Where does execution time go? [0.25pts] ------------------------------#
#########################################################################################################
'''
Output:


         69 function calls (24 primitive calls) in 8.213 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    55/10    0.000    0.000    0.000    0.000 ex3.py:30(sub_function)
        1    0.000    0.000    0.000    0.000 ex3.py:38(test_function)
        1    0.000    0.000    8.213    8.213 ex3.py:45(third_function)
        1    8.213    8.213    8.213    8.213 ex3.py:47(<listcomp>)
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Answer:
    From the sample output we can notice that despite the sub_function() being called multiple times
    it barely takes any time, Whereas the the third_function() takes the majourity of the programs 
    execution time so if we had to optimize to run faster the code we should start there. 

'''

