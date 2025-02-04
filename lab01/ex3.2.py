import timeit
import json
import numpy as np 
from matplotlib import pyplot as plt

with open('lab_data/large-file.json', 'r', encoding='UTF-8') as infile: 
    data = json.load(infile)



def change_size(data, size=42, num_records=10000):
    records = num_records
    for record in data: 
        if 'size' in record: 
            record['size'] = size
        if records == 0: 
            break
        records -= 1



num_records = [1000, 2000, 5000, 10000]
avg_times = []


for num in num_records:
    time_to_change = timeit.timeit(lambda: change_size(data, num_records=num), number=100, setup="import json")
    time_to_change /= 100
    avg_times.append(time_to_change)
    print(f"time to change: {time_to_change}")

slope, intercept = np.polyfit(num_records, avg_times, 1)
plt.scatter(num_records, avg_times)
linevalues = [slope * x + intercept for x in num_records]
plt.plot(num_records, linevalues, 'r')
plt.savefig('output.3.2.png')

infile.close()



print("done")


