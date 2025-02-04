import timeit
import json

with open('lab_data/large-file.json', 'r', encoding='UTF-8') as infile: 
    data = json.load(infile)



def change_size(data, size=42):
    for record in data: 
        if 'payload' in record and 'size' in record['payload']: 
            record['payload']['size'] = size

change_size(data)

time_to_change = timeit.timeit(lambda: change_size(data), number=10, setup="import json")
time_to_change /= 10
    
reversed_data = tuple(reversed(data))

with open('lab_data/output2.3.json', 'w', encoding='UTF-8') as outfile: 
    json.dump(reversed_data, outfile)

outfile.close()
infile.close()



print(f" time for 10 runs of change_size(): {time_to_change}")


