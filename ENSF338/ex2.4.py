import timeit

def average_vowels():
    vowels = ['a', 'i', 'o', 'e', 'u', 'y']
    sum_of_vowels = 0
    word_count = 0
    start = False  
    file.seek(0)
    
    for line in file:
        if line.strip() == "CHAPTER 1. Loomings." or start:
            start = True
            word_count += len(line.split()) 
            for char in line.lower():
                if char in vowels:
                    sum_of_vowels += 1
    return sum_of_vowels / word_count

def time_vowel_computation():
    timer = timeit.Timer("average_vowels()", setup="from __main__ import average_vowels")
    total_time = timer.timeit(number=100)
    print(f"Average time across 100 repetitions: {total_time / 100} seconds")



file = open(r"C:\ENSF338\pg2701.txt", "r", encoding="UTF-8")
    
time_vowel_computation()

file.close()