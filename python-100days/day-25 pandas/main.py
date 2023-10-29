# with open(r'day-25 pandas\weather_data.csv', 'r') as f:
#     data = f.read().splitlines()
#     print(data)

#TODO: use csv module to read csv file
# import csv

# with open(r'day-25 pandas\weather_data.csv', 'r') as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

#TODO: read csv file with pandas

import pandas as pd

data = pd.read_csv(r'day-25 pandas\weather_data.csv')

# print(data['temp'][0])
# print(data.to_dict())
# print(sum(data['temp'].to_list())/len(data))
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data.condition, data.temp)

# print('Max:',data[data.temp == data.temp.max()])
# print('On Monday',data[data.day == 'Monday'])


#TODO: Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }

# data = pd.DataFrame(data_dict)
# print(data)

#TODO: Create a dataframe from a csv file and get data
data = pd.read_csv(r'day-25 pandas\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray = data[data['Primary Fur Color'] == 'Gray']['Primary Fur Color'].count()
print(gray)
red = data[data['Primary Fur Color'] == 'Cinnamon']['Primary Fur Color'].count()
print(red)
black = data[data['Primary Fur Color'] == 'Black']['Primary Fur Color'].count()
print(black)

data_dict = {
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count':[gray, red, black]
    
}
df=pd.DataFrame(data_dict)
df.to_csv(r'day-25 pandas\squirrel_count.csv',index=False,header=True)