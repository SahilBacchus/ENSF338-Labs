import timeit
import json
import numpy as np 
from matplotlib import pyplot as plt

with open('lab01/lab_data/large-file.json', 'r', encoding='UTF-8') as infile: 
    data = json.load(infile)



def change_size(data, size=42, num_records=10000):
    records = num_records
    for record in data: 
        if 'payload' in record and 'size' in record['payload']: 
            record['payload']['size'] = size
        if records == 0: 
            break
        records -= 1



times = timeit.repeat(lambda: change_size(data, num_records=1000), number=1, repeat=1000, setup="import json")

plt.hist(times, rwidth=0.7)
plt.title('Distribution of Time to Process First 1000 Records')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.savefig('lab01/output.3.3.png')

infile.close()



print("done")


