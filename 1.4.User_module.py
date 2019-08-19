print('ANALYZING CRIME')
print('\nImporting required libraries...')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt 
import os
import webbrowser
import numpy as np 
import folium

print('Importing Dataset...')
crimes = read_csv('Chicago_Crimes_2012_to_2017.csv', index_col='Date')
print('\nPreprocessing data...')
symbol = (())

ctype = input('Enter the crime you want to annalyze: ')
cr_crime = crimes.loc[crimes['Primary Type'] == ctype, ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location', 'Community Area']]

#1st Plot
print('Annalyzing the number of cases which led to an arrest (Arrested / Not Arrested):')
labels = ['False', 'True']
fig1, ax1 = plt.subplots()
fig1.suptitle('Percentage of Successful Arrests', fontsize = 16)

arrest_count = pd.DataFrame(cr_crime.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ax1.set_title(ctype)

x = input('press ENTER to view pie chart.')
plt.setp(fig1.axes, yticks=[])
plt.show()

print('Annalyzing the number of Domestic crimes in this three particular crimes:')
labels = ['False', 'True']
fig2, ax = plt.subplots()
fig2.suptitle('Percentage of Domestic Crimes', fontsize = 16)

Domestic_count = pd.DataFrame(cr_crime.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())
sizes = Domestic_count['count'].tolist()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax.set_title(ctype) 

x = input('press ENTER to view pie chart.')
plt.setp(fig2.axes, yticks=[])
plt.show()

print('Top five location in which the crime took place maximum.')
loc_crime = pd.DataFrame(cr_crime.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
loc_crime = loc_crime.ix[:4,:]


fig3, ax1 = plt.subplots()
ti = 'Top 5 locations of '+ ctype
fig3.suptitle(ti)

sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=loc_crime, label="Location", palette = 'Dark2', ax = ax1)
ax1.set(ylabel="Crimes", xlabel="Location")
ax1.axhline(0, color="k", clip_on=False)


sns.despine(bottom=True)
plt.setp(ax1.get_xticklabels(), rotation=45)
x = input('Press ENTER to view the graph.')
plt.show()

vis = os.path.join('Community_Areas.json')
com_count = pd.DataFrame(cr_crime.groupby('Community Area').size().sort_values(ascending=False).rename('count').reset_index())
com_count['Community Area'] = com_count['Community Area'].astype('int').astype('str')

Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")
Chicago_map.choropleth(geo_data=vis, data = com_count, columns = ['Community Area', 'count'], name='choropleth', fill_color = 'Reds', fill_opacity = '0.9', key_on = 'feature.properties.area_numbe', line_weight = '1')

folium.LayerControl().add_to(Chicago_map)
filepath = 'Crime_Choropleth.html'
Chicago_map.save(filepath)
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)
