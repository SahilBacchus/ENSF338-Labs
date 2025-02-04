import timeit

def pow2(n):
    return 2**n

def pow2_acs(n):
    for i in range(n+1):
        calculate = 2**i
    return 0

def pow2_list_comp(n):
    return [2**i for i in range(n+1)]

def time_pow2_computation():
    timer = timeit.Timer(f"pow2({10000})", setup="from __main__ import pow2")
    total_time = timer.timeit(number=10000)
    print(f"Time(2^n): {total_time} seconds")

def time_pow2_asc_computation():
    timer = timeit.Timer(f"pow2_acs({1000})", setup="from __main__ import pow2_acs")
    total_time = timer.timeit(number=1000)
    print(f"Time (For loop): {total_time} seconds")

def time_pow2_list_comp_computation():
    timer = timeit.Timer(f"pow2_list_comp({1000})", setup="from __main__ import pow2_list_comp")
    total_time = timer.timeit(number=1000)
    print(f"Time (List Comprehension): {total_time} seconds")



time_pow2_computation()
time_pow2_asc_computation()
time_pow2_list_comp_computation()

