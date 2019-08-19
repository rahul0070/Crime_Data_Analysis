print('ANALYZING CRIME')
print('\nImporting required libraries.')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt 
import os
import webbrowser
import numpy as np 
import folium
from gtts import gTTS 
from playsound import playsound
from sklearn.cluster import KMeans
import threading
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn import tree
import time

def clear():
    os.system( 'cls' )

gTTS(text='Enter the crime you want to annalyze', lang='en', slow=False).save('Audio/input.mp3')
gTTS(text='Press enter to view the result', lang='en', slow=False).save('Audio/output.mp3')
def audio1():
	playsound('Audio/input.mp3')

def audio2():
	playsound('Audio/output.mp3')

def audio3():
	playsound('Audio/output_2.mp3')
	time.sleep(2)
	playsound('Audio/output.mp3')

print('Importing Dataset...')
crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv')
print('\nPreprocessing data...')
symbol = (())

t1 = threading.Thread(target=audio1)
t1.start()
ctype = input('Enter the crime you want to annalyze: ')
clear()
cr_crime = crimes.loc[crimes['Primary Type'] == ctype, ['Date', 'Primary Type', 'Arrest', 'Domestic', 'Location Description', 'Location', 'Community Area', 'District']]
#1st Plot
Dist = ['Central', 'Wentworth', 'Grand Crossing', 'South Chicago', 'Calumet', 'Gresham', 'Englewood', 'Chicago Lawn', 'Deering', 'Ogden', 'Harrison', 'Near West', 'Shakespeare', 'Austin', 'Jefferson Park', 'Albany Park', 'Near North', 'Town Hall', 'Lincoln', 'Morgan Park', 'Rogers Park', 'Grand Central']

fig1, ax1 = plt.subplots(figsize=(12, 14))
sns.set(style="darkgrid")
dist_count = pd.DataFrame(cr_crime.groupby('District').size().sort_values(ascending=False).rename('count').reset_index())
sns.barplot(x="District", y="count", data=dist_count, label="Total", palette = 'Dark2', ax = ax1)
plt.xlabel('Districts')
plt.ylabel('Number of Crimes')
plt.title('Districts with top count of the crime ')
plt.xticks(dist_count['District'].sort_values(ascending = True), Dist, rotation = 50)
#sns.despine(left=True, bottom=True)
plt.show()

hour = []
for x in range(0, 25):
	hour.append(str(x))


crimes = cr_crime
crimes.Date = pd.to_datetime(crimes.Date, format = '%m/%d/%Y %I:%M:%S %p')
crimes.index = pd.DatetimeIndex(crimes.Date)
crimes.insert(3, 'Hour', 'NULL')
crimes['Hour'] = crimes.index.hour

print('\nIMPLEMENTING K-MEAN CLUSTERING ALGORITHM')
print('We are clustering the different hours of a day based on the number of crimes commited in the particular hour.')
print('\nPreprocessing data.')
Hour_count = pd.DataFrame(crimes.groupby('Hour').size().sort_values(ascending=False).rename('Counts').reset_index())

print('\nFitting the data in KMeans algorithm.')
kmean = KMeans(n_clusters = 3)
kmean.fit(Hour_count)
pr = kmean.predict(Hour_count)
print(pr)
centers = kmean.cluster_centers_
print('\nPlotting graph...')
plt.figure(figsize=(8,6))
plt.scatter(Hour_count['Hour'], Hour_count['Counts'], c=pr, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.xlabel('Hours')
plt.ylabel('Number of Crimes')
ti = 'K-Means Clustering of ' + ctype
plt.title(ti)
s = Hour_count['Hour'].sort_values(ascending=True)
plt.xticks(s, hour)
t2 = threading.Thread(target=audio3)
t2.start()
x = input('Press ENTER to view graph.')
plt.show()
clear()

cluster_map = pd.DataFrame()
cluster_map['data_index'] = Hour_count['Hour']
cluster_map['cluster'] = kmean.labels_

l0 = []
l1 = []
l2 = []
li1 = cluster_map['cluster'].tolist()
li2 = cluster_map['data_index'].tolist()



crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv')
crimes = crimes.dropna()
cr_crime = crimes.loc[crimes['Primary Type'] == ctype, :]
crimes.Date = pd.to_datetime(crimes.Date, format = '%m/%d/%Y %I:%M:%S %p')
crimes.index = pd.DatetimeIndex(crimes.Date)
crimes.insert(3, 'Hour', 'NULL')
crimes['Hour'] = crimes.index.hour
crimes.insert(3, 'Value', 'NULL')

for i in range(24):
	if li1[i] == 0:
		l0.append(li2[i])

	if li1[i] == 1:
		l1.append(li2[i])

	if li1[i] == 2:
		l2.append(li2[i])

print(l0)
print(l1)
print(l2)

for i in l0:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'a'

for i in l1:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'b'

for i in l2:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'c'

ti1 = 'Hours: '+ str(l0)
ti2 = 'Hours: '+ str(l1)
ti3 = 'Hours: '+str(l2)

cr_a = crimes.loc[crimes['Value'] == 'a', :]
cr_b = crimes.loc[crimes['Value'] == 'b', :]
cr_c = crimes.loc[crimes['Value'] == 'c', :]

labels = ['False', 'True']
fig2, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 6), sharex = True)
fig2.suptitle('Percentage of Arrests', fontsize = 15)

arrest_count = pd.DataFrame(cr_a.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90) 
ax1.set_title(ti1)

arrest_count = pd.DataFrame(cr_b.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax2.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax2.set_title(ti2)

arrest_count = pd.DataFrame(cr_c.groupby('Arrest').size().sort_values(ascending=False).rename('count').reset_index())
sizes = arrest_count['count'].tolist()
ax3.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax3.set_title(ti3)

x = input('press ENTER to view pie chart.')
plt.setp(fig2.axes, yticks=[])
plt.show()

print(crimes['Arrest'])
df1 = crimes.loc[:,['Arrest', 'Value']]
le = preprocessing.LabelEncoder()

df1['Arrest'] = le.fit_transform(df1['Arrest'].tolist())
d2 = dict(zip(le.classes_, le.transform(le.classes_)))

df1['Value'] = le.fit_transform(df1['Value'].tolist())
d3 = dict(zip(le.classes_, le.transform(le.classes_)))

pr_data = df1[['Value']]
pr_target = df1[['Arrest']]

gnb = tree.DecisionTreeClassifier()
y_pred = gnb.fit(pr_data, pr_target).predict(pr_data)
print(gnb.predict([[0]]))
print(d3)
s1 = 0
s2 = 0
for ix in range(500):
	if gnb.predict([[0]]) == 1:
		s1 = s1+1
		s2 = s2+1
	else:
		s2 = s2+1

print(s1/(s1+s2))


print('\nAccuracy: ', gnb.score(pr_data, pr_target)*100, '%')
clear()




vis = os.path.join('Data/Community_Areas.json')
vis2 = os. path.join('Data/Ward.geojson')
com_count = pd.DataFrame(cr_crime.groupby('Community Area').size().sort_values(ascending=False).rename('count').reset_index())
com_count['Community Area'] = com_count['Community Area'].astype('int').astype('str')

Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")
Chicago_map.choropleth(geo_data=vis, data = com_count, columns = ['Community Area', 'count'], name='choropleth', fill_color = 'Reds', fill_opacity = '0.9', key_on = 'feature.properties.area_numbe', line_weight = '1')

folium.LayerControl().add_to(Chicago_map)
filepath = 'Crime_Choropleth.html'
Chicago_map.save(filepath)
t3 = threading.Thread(target=audio3)
t3.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)


com_count = pd.DataFrame(cr_crime.groupby('Ward').size().sort_values(ascending=False).rename('count').reset_index())
com_count['Ward'] = com_count['Ward'].astype('int').astype('str')
Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 11, tiles = "CARTODBPOSITRON")

Chicago_map.choropleth(geo_data=vis2, data = com_count, columns = ['Ward', 'count'], name='choropleth', fill_color = 'Blues', fill_opacity = '0.9', key_on = 'feature.properties.ward', line_weight = '1')

folium.LayerControl().add_to(Chicago_map)
filepath = 'Ward_Choropleth.html'
Chicago_map.save(filepath)
t4 = threading.Thread(target=audio3)
t4.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)



