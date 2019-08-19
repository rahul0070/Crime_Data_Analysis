print('ANALYZING MONTH WISE CRIME DATA:')
print('\nImporting required libraries.')
print('Importing Dataset.')
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import calendar
import seaborn as sns
from pandas import read_csv

print('\nIMPLEMENTING K-MEAN CLUSTERING ALGORITHM')
print('We are clustering the different months of the years based on the number of crimes commited in a certain month.')
print('\nPreprocessing Data.')
month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv',error_bad_lines=False)
crimes.Date = pd.to_datetime(crimes.Date, format = '%m/%d/%Y %I:%M:%S %p')
crimes.index = pd.DatetimeIndex(crimes.Date)

crimes.insert(3, 'Month', 'NULL')
crimes['Month'] = crimes.index.month

print('\nSelecting the required attributes.')
Month_count = pd.DataFrame(crimes.groupby('Month').size().sort_values(ascending=False).rename('Counts').reset_index())

print('\nFitting the data in KMeans algorithm.')
kmean = KMeans(n_clusters = 2)
kmean.fit(Month_count)
pr = kmean.predict(Month_count)
centers = kmean.cluster_centers_

print('Plotting graph.')
plt.figure(figsize=(8,6))
sns.set(style="darkgrid")
plt.scatter(Month_count['Month'], Month_count['Counts'], c=pr, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.xlabel('Months')
plt.ylabel('Number of Crimes')
plt.title('K-Means Clustering ')
plt.xticks(Month_count['Month'], month, rotation = 50)
x = input('Press enter to view the graph.')
plt.show()

cluster_map = pd.DataFrame()
cluster_map['data_index'] = Month_count['Month']
cluster_map['cluster'] = kmean.labels_
print(cluster_map)

l0 = []
l1 = []

li1 = cluster_map['cluster'].tolist()
li2 = cluster_map['data_index'].tolist()

for i in range(12):
	if li1[i] == 0:
		l0.append(li2[i])

	if li1[i] == 1:
		l1.append(li2[i])

print(l0)
print(l1)

crimes.insert(3, 'Value', 'NULL')
for i in l0:
	crimes.loc[crimes['Month'] == i, ['Value']] = 'a'

for i in l1:
	crimes.loc[crimes['Month'] == i, ['Value']] = 'b'

cr_a = crimes.loc[crimes['Value'] == 'a', ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location']]
cr_b = crimes.loc[crimes['Value'] == 'b', ['Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location']]

a_pt = pd.DataFrame(cr_a.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
a_pt = a_pt.ix[:5,:]

b_pt = pd.DataFrame(cr_b.groupby('Primary Type').size().sort_values(ascending=False).rename('count').reset_index())
b_pt = b_pt.ix[:5,:]

#3rd plot
labels = ['False', 'True']
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), sharex = True)
fig2.suptitle('Percentage of Successful Arrests', fontsize = 15)

print('GROUP 1 = Months of : ', l0)
print('GROUP 2 = Months of : ', l1)
arrest_count = pd.DataFrame(cr_a.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ti1 = 'Months: '+ str(l0)
ax1.set_title(ti1)

arrest_count = pd.DataFrame(cr_b.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ti2 = 'Months: '+ str(l1)
ax2.set_title(ti2)

x = input('press ENTER to view pie chart.')
plt.setp(fig2.axes, yticks=[])
plt.show()

x = input('Press any key to exit.')
