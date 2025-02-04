import json
import matplotlib.pyplot as plt
# open JSON file & load content
with open('c:/Users/nolan/ENSF338/assignment01/lab_data/internetdata.json', 'r') as file:
    data = json.load(file)

# create 2 lists to store each dataset
group1 = []
group2 = []

for country_data in data:
    # handle scenario when incomeperperson is null
    if country_data['incomeperperson'] is not None:
        if country_data['incomeperperson'] < 10000:
            group1.append(country_data)
        elif country_data['incomeperperson'] >= 10000:
            group2.append(country_data)
        else:
            print('Invalid')
        
# iterate through each list and store internetuserate for each country
# in corresponding lists
# add is not None at the end to ensure no null values
group1_internet_usage = [country['internetuserate'] for country in group1 if country['internetuserate'] is not None]
group2_internet_usage = [country['internetuserate'] for country in group2 if country['internetuserate'] is not None]

plt.figure(figsize=(12, 6))
#Histogram 1
plt.subplot(1, 2, 1)
plt.hist(group1_internet_usage, bins = 15, color = 'skyblue', edgecolor = 'black')
plt.title('Histogram for Countries with Income Below 10000')
plt.xlabel('Internet Usage Rate (%)')
plt.ylabel('Frequency')

#Histogram 2
plt.subplot(1, 2, 2)
plt.hist(group2_internet_usage, bins = 15, color = 'red', edgecolor = 'black')
plt.title('Histogram for Countries with Income at or Above 10000')
plt.xlabel('Internet Usage Rate (%)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
