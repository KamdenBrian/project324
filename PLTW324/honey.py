import matplotlib.pyplot as mat
import pandas as pd
import math

df = pd.read_csv('honey.csv', header=0)
df['Value'] = df['Value'].str.replace(',', '')
df['Value'] = pd.to_numeric(df['Value'], errors = 'coerce')
df.dropna(subset =['Value'], inplace=True)

all_honey = []
all_states = []
all_sum = []

unique_states = df['State'].unique()
unique_years = df['Year'].unique()

for state in unique_states:
    honey_data = df[df['State'] == state].groupby('Year')['Value']
    all_honey.append(honey_data.mean())
    all_states.append(state)

for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    honey_data = df[df['State'] == state]['Value']
    if(honey_data.sum() > 7500000):
        years = honey.keys()
        mat.plot(years, honey, label = state, marker='o', linestyle=':')
mat.ylabel('Amount of honey made')
mat.xlabel('Year')
mat.title('Large state producers')
mat.legend()
mat.show()


for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    honey_data = df[df['State'] == state]['Value']
    if(honey_data.sum() > 2500000 and not(honey_data.sum() > 7500000)):
        years = honey.keys()
        mat.plot(years, honey, label = state, marker='v', linestyle='-.')
    
mat.ylabel('Amount of honey made')
mat.xlabel('Year')
mat.title('Medium state producers')
mat.legend()
mat.show()

for i in range(len(all_states)):
    honey = all_honey[i]
    state = all_states[i]
    honey_data = df[df['State'] == state]['Value']
    if(honey_data.sum() < 2500000):
        years = honey.keys()
        mat.plot(years, honey, label = state, marker='^', linestyle='--')

mat.ylabel('Amount of honey made')
mat.xlabel('Year')
mat.title('Small state producers')
mat.legend()
mat.show()

for year in unique_years:
    totals = df[df['Year'] == year].groupby('Year')['Value']
    all_sum.append(totals.sum())

for i in range(len(unique_years)):
    total = all_sum[i]
    years = total.keys()
    mat.bar(years, total)
mat.ylabel('Amount of honey made')
mat.xlabel('Year')
mat.title('Total honey made each year')
mat.show()