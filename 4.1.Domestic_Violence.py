print('Including required libraries.')
print('Importing CSV file into dataframe.')

import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

crimes = read_csv('Chicago_Crimes_2012_to_2017.csv', index_col='Date')
print('\nData type: ', type(crimes))

print('Removing NULL values.')
symbol = (())

#1st plot
Domestic_count = pd.DataFrame(crimes.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())

sizes = Domestic_count['count'].tolist()
labels = ['False', 'True']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.title('Percentage of Domestic crimes')
x = input('\nPress ENTER to view pie chart.')
plt.show()

#2nd plot
cr_domestic = crimes.loc[crimes['Domestic'] == True, ['Primary Type', 'Domestic', 'Arrest', 'Location Description']]
cr_domestic_f = crimes.loc[crimes['Domestic'] == False, ['Primary Type', 'Domestic', 'Arrest', 'Location Description']]

pr = pd.DataFrame(cr_domestic.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
ld = pd.DataFrame(cr_domestic.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())

pr = pr.ix[:4,:]
ld = ld.ix[:4,:]

sns.set(style="darkgrid")
sns.set_color_codes("dark")
sns.barplot(x="Primary Type", y="count", data=pr, label="Total", palette = 'Set1').set(ylabel="Count", xlabel="Type of Crime", title = 'Top 5 types of domestic crimes')
plt.xticks(rotation = 50)
plt.show()

sns.set(style="darkgrid")
sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=ld, label="Total", palette = 'Set1').set(ylabel="Count", xlabel="Location Description", title = 'Top 5 location of domestic crimes')
plt.xticks(rotation = 50)
plt.show()

#3rd plot
labels = ['False', 'True']
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex = True)
fig1.suptitle('Percentage of successful Arrests', fontsize = 15)

arrest_count1 = pd.DataFrame(cr_domestic.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes1 = arrest_count1['count'].tolist()
ax1.pie(sizes1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ax1.set_title('Domestic')

arrest_count2 = pd.DataFrame(cr_domestic_f.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes2 = arrest_count2['count'].tolist()
ax2.pie(sizes2, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.set_title('Non Domestic')

x = input('press ENTER to view pie chart.')
plt.setp(fig1.axes, yticks=[])
plt.show()
