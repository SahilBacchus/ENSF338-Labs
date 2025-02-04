import json

with open('lab_data/large-file.json', 'r', encoding='UTF-8') as file: 
    data = json.load(file)



for record in data: 
    if 'size' in record: 
        record['size'] = 42


    
reversed_data = tuple(reversed(data))

with open('lab_data/output2.3.json', 'w', encoding='UTF-8') as file: 
    json.dump(reversed_data, file)


print("done")

file.close()



