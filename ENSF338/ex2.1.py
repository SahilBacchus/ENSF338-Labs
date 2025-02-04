import sys
import math
 # (i) The code calculates the roots of quadratic equation using 
 #     the given values, as long as the equation produces a real
 #     root

#(ii) The code has incorrect quotation marks which resulted in
#     various issues as syntax was being considered text and
#     was causing the code to fail
#     Also can't divide by 0, which causes and error

def do_stuff():
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')
do_stuff()