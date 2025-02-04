import json

with open('lab01/lab_data/large-file.json', 'r', encoding='UTF-8') as file: 
    data = json.load(file)



for record in data: 
    if 'payload' in record and 'size' in record['payload']: 
        record['payload']['size'] = 42


    
reversed_data = tuple(reversed(data))

with open('lab01/lab_data/output2.3.json', 'w', encoding='UTF-8') as file: 
    json.dump(reversed_data, file, indent=2)


print("done")

file.close()



