print('ANNALYZING THEFTS, ASSAULTS AND HOMICIDE.\n')
print('\nImporting required libraries.')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt 

print('Importing Dataset.')
crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')
print('\nPreprocessing data.')
symbol = (())

cr_theft = crimes.loc[crimes['Primary Type'] == 'THEFT', ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location']]
cr_assault = crimes.loc[crimes['Primary Type'] == 'ASSAULT', ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location']]
cr_homicide = crimes.loc[crimes['Primary Type'] == 'HOMICIDE', ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location']]

#1st Plot
print('Annalyzing the number of cases which led to an arrest (Arrested / Not Arrested):')
labels = ['False', 'True']
fig1, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6), sharex = True)
fig1.suptitle('Percentage of Successful Arrests', fontsize = 16)

arrest_count = pd.DataFrame(cr_theft.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ax1.set_title('Thefts')

arrest_count = pd.DataFrame(cr_assault.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.set_title('Assaults')

arrest_count = pd.DataFrame(cr_homicide.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.set_title('Homicide') 

x = input('press ENTER to view pie chart.')
plt.setp(fig1.axes, yticks=[])
plt.show()

print('Annalyzing the number of Domestic crimes in this three particular crimes:')
labels = ['False', 'True']
fig2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6), sharex = True)
fig2.suptitle('Percentage of Domestic Crimes', fontsize = 16)

Domestic_count = pd.DataFrame(cr_theft.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())
sizes = Domestic_count['count'].tolist()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.set_title('Thefts') 

Domestic_count = pd.DataFrame(cr_assault.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())
sizes = Domestic_count['count'].tolist()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.set_title('Assaults')

Domestic_count = pd.DataFrame(cr_homicide.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())
sizes = Domestic_count['count'].tolist()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.set_title('Homicide')

x = input('press ENTER to view pie chart.')
plt.setp(fig2.axes, yticks=[])
plt.show()

print('Top five location in which each of the three crime took place maximum.')
loc_theft = pd.DataFrame(cr_theft.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
loc_theft = loc_theft.ix[:4,:]

loc_assault = pd.DataFrame(cr_assault.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
loc_assault = loc_assault.ix[:4,:]

loc_homicide = pd.DataFrame(cr_homicide.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
loc_homicide = loc_homicide.ix[:4,:]


fig3, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6), sharex = True)
fig3.suptitle('Top 5 locations of Thefts, Assaults and Homicide.')

sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=loc_theft, label="Location", palette = 'Dark2', ax = ax1)
ax1.set(ylabel="Crimes", xlabel="Location")
ax1.axhline(0, color="k", clip_on=False)
ax1.set_title('Thefts')

sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=loc_assault, label="Location", palette = 'Dark2', ax = ax2)
ax2.set(ylabel="Crimes", xlabel="Location")
ax2.axhline(0, color="k", clip_on=False)
ax2.set_title('Assaults')

sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=loc_homicide, label="Location", palette = 'Dark2', ax = ax3)
ax3.set(ylabel="Crimes", xlabel="Location")
ax3.axhline(0, color="k", clip_on=False)
ax3.set_title('Homicide')

sns.despine(bottom=True)
#plt.setp(fig3.axes, yticks=[])
plt.setp(ax1.get_xticklabels(), rotation=45)
plt.setp(ax2.get_xticklabels(), rotation=45)
plt.setp(ax3.get_xticklabels(), rotation=45)
x = input('press ENTER to view the graph.')
plt.show()
