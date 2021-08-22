import pandas as pd 


data = pd.read_csv('abalone.data')
columns_names = ['Sex', 'Length', 'Diameter', 'Height', 'Whole', 'weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

# pd.set_option('display.max_rows', data.shape[0]+1)
# print(data)

print(data.head(len(data.index)))
