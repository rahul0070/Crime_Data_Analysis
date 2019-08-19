print('Including required libraries.')
print('Importing CSV file into dataframe.')

import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')

#1st plot
arrest_count = pd.DataFrame(crimes.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
print('Looking the number of arrests for all kind of crimes.')
print('\nPlotting the graph.')

sizes = arrest_count['count'].tolist()
labels = ['False', 'True']
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal') 
plt.title('Percentage of Successful Arrests')
x = input('press ENTER to view pie chart.')
plt.show()

#2nd plot
cr_true = crimes.loc[crimes['Arrest'] == True, ['Primary Type', 'Arrest', 'Location Description', 'Community Area']]
cr_false = crimes.loc[crimes['Arrest'] == False, ['Primary Type', 'Arrest', 'Location Description', 'Community Area']]

ar_tr = pd.DataFrame(cr_true.groupby('Primary Type').size().sort_values(ascending=False).rename('count1').reset_index())
ar_fa = pd.DataFrame(cr_false.groupby('Primary Type').size().sort_values(ascending=False).rename('count2').reset_index())

val3 = []
val4 = []
val1 = ar_tr['count1'].tolist()
val2 = ar_fa['count2'].tolist()
nam = ar_tr['Primary Type'].tolist()

for i in range(30):
	x = val1[i]/ (val1[i] + val2[i])
	x = x*100
	val3.append(x)

for i in range(30):
	x = val2[i]/ (val1[i] + val2[i])
	x = x*100
	val4.append(x)

cr1 = pd.DataFrame({'Primary Type': nam[:30], 'count':val3[:30]})
cr2 = pd.DataFrame({'Primary Type': nam[:30], 'count':val4[:30]})


t_pt = pd.DataFrame(cr_true.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
t_pt = t_pt.ix[:5,:]
f_pt = pd.DataFrame(cr_false.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
f_pt = f_pt.ix[:5,:]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex = True)

cr1 = cr1.sort_values(by=['count'], ascending=False)
cr2 = cr2.sort_values(by=['count'], ascending=False)
cr1 = pd.DataFrame(cr1).reset_index()
cr2 = pd.DataFrame(cr2).reset_index()

cr1 = cr1.ix[:5,:]
cr2 = cr2.ix[:5,:]

print('\nHIGHEST SUCCESSFUL ARREST PERCENTAGE')
print(cr1)
print('\n')
print('HIGHEST UNSUCCESSFUL ARREST PERCENTAGE')
print(cr2)

sns.set_color_codes("dark")
sns.barplot(x="Primary Type", y="count", data=cr1, palette = 'Dark2', ax = ax1)
ax1.set(ylabel="Crimes", xlabel="Type of crime")
ax1.set_title('Successful Arrests')

sns.set_color_codes("dark")
sns.barplot(x="Primary Type", y="count", data=cr2, palette = 'Dark2', ax = ax2)
ax2.set(ylabel="Crimes", xlabel="Type of crime")
ax2.set_title('Unsuccessful Arrests')

sns.despine(bottom=True)
plt.setp(ax1.get_xticklabels(), rotation=45)
plt.setp(ax2.get_xticklabels(), rotation=45)
x = input('press ENTER to view the graph.')
plt.show()

#3rd plot
t_ld = pd.DataFrame(cr_true.groupby('Location Description').size().sort_values(ascending=False).rename('count').reset_index())
t_ld = t_ld.ix[:5,:]

print(t_ld)
fig, ax = plt.subplots()
sns.set_color_codes("dark")
sns.barplot(x="Location Description", y="count", data=t_ld, label="Location", palette = 'Set1', ax = ax)
ax.set(ylabel="Crimes", xlabel="Location")
ax.axhline(0, color="k", clip_on=False)
ax.set_title('Successful Arrests')
plt.xticks(rotation = 50)
x = input('press ENTER to view the graph.')
plt.show()

#4th plot
t_c = pd.DataFrame(cr_true.groupby('Community Area').size().sort_values(ascending=False).rename('count').reset_index())
t_c = t_c.ix[:9,:]
print('\nPlotting the graph.')

sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(13, 10))
sns.set_color_codes("dark")
sns.barplot(x="Community Area", y="count", data=t_c, label="Community", palette = 'Paired')
ax.set(ylabel="Crimes", xlabel="Community")
ax.set_title('Top 10 locations')
sns.despine(left=True, bottom=True)
plt.xticks(rotation = 50)
x = input('press ENTER to view the graph.')
plt.show()
