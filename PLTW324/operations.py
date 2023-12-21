import matplotlib.pyplot as mat
import pandas as pd
import math

df = pd.read_csv('operations.csv', header=0)


all_states = []
all_sum = []
all_operations = []

unique_states = df['State'].unique()
unique_years = df['Year'].unique()

for state in unique_states:
    operation_data = df[df['State'] == state].groupby('Year')['Value']
    all_operations.append(operation_data.sum())
    all_states.append(state)

for i in range(len(all_states)):
    operation = all_operations[i]
    state = all_states[i]
    years = operation.keys()
    mat.plot(years, operation, label = state)
mat.ylabel('Honey Production Facilities')
mat.xlabel('Year')
mat.title('Facilities in each state')
mat.legend()
mat.show()

for year in unique_years:
    totals = df[df['Year'] == year].groupby('Year')['Value']
    all_sum.append(totals.sum())

for i in range(len(unique_years)):
    total = all_sum[i]
    years = total.keys()
    mat.bar(years, total)
mat.ylabel('Honey Production Facilities')
mat.xlabel('Year')
mat.title('Facilities across each year')
mat.legend()
mat.show()