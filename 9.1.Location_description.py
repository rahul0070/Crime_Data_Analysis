print('ANALYZING LOCATIONS.')
print('\nImporting required libraries.')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt 

print('Importing Dataset.')
crimes = read_csv('Chicago_Crimes_2012_to_2017.csv', index_col='Date')
print('\nPreprocessing data.')
symbol = (())

loc_count = pd.DataFrame(crimes.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
loc_count = loc_count.ix[:6,:]

sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6, 15))
f.suptitle('Locations')

sns.set_color_codes("pastel")
sns.barplot(x="Location Description", y="count", data=loc_count, label="Total", palette = "tab10")
ax.set(ylabel="Number of crimes commited", xlabel="Crimes")
sns.despine(left=True, bottom=True)
plt.setp(ax.get_xticklabels(), rotation=45)
x = input('\nPress ENTER to view graph.')
plt.show()


cr_st = crimes.loc[crimes['Location Description'] == 'STREET', ['Primary Type', 'Domestic', 'Arrest', 'Location Description']]
cr_r = crimes.loc[crimes['Location Description'] == 'RESIDENCE', ['Primary Type', 'Domestic', 'Arrest', 'Location Description']]

labels = ['False', 'True']
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex = True)
fig1.suptitle('Percentage of Domestic crimes', fontsize = 15)

dom_count1 = pd.DataFrame(cr_st.groupby('Domestic').size().sort_values(ascending=False).rename('count').reset_index())
sizes1 = dom_count1['count'].tolist()
ax1.pie(sizes1, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ax1.set_title('Street')

dom_count2 = pd.DataFrame(cr_r.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes2 = dom_count2['count'].tolist()
ax2.pie(sizes2, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.set_title('Residence')

x = input('press ENTER to view pie chart.')
plt.setp(fig1.axes, yticks=[])
plt.show()