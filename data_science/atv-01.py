import pandas as pd 


data = pd.read_csv('abalone.data')

print(data)

columns_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole', 'weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

while(data):
    for row in data: 
        print(row)