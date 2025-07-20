#uncomment respective sections to run only(running everythin at the same time may run into some issues)

import pandas as pd
import matplotlib.pyplot as mt

data = pd.read_csv('large_employees.csv')

#PANDAS
# calculating the average
avg_sal = data['Salary'].mean()

#print('Average Salary: ',avg_sal)

#counting entries

cities_count = data['City'].value_counts()

#print('total no. employees in a city: ','\n',cities_count)

#filter

above_1lakh = data[data['Salary'] > 100000]

#print('no. of employess with slaries above 1 lakh: ','\n',above_1lakh)

#maximum and minimum

max_sal = data['Salary'].max()
min_sal = data['Salary'].min()

#print('The maximum Salary is:',max_sal,'&','minimum Salary is:',min_sal)

#MATPLOTLIB
#BAR GRAPH

dep_avg_sal = data.groupby('Department')['Salary'].mean().sort_values()

mt.figure(figsize=(10,10))

#dep_avg_sal.plot(kind='bar',color='red')

#mt.title('Avg salary of each department')

#mt.show()

#SCATTER PLOT

#mt.scatter(data['Age'],data['Salary'],color='blue')

#mt.title('age v salary')

#mt.grid(True)

#mt.xlabel('Age')

#mt.ylabel('Salary')

#mt.show()

#HEATMAP

#corrmat = data[['Age','Salary','Experience']].corr()

#mt.imshow(corrmat, cmap='coolwarm')

#mt.title('correlation heatmap')

#mt.xticks(range(len(corrmat)), corrmat.columns,)

#mt.yticks(range(len(corrmat)), corrmat.columns)

#mt.colorbar

#for i in range(len(corrmat)):
#    for j in range(len(corrmat)):
#        text = f"{corrmat.iloc[i, j]:.2f}"
#        mt.text(j, i, text, ha='center', va='center', color='black')

#mt.show()