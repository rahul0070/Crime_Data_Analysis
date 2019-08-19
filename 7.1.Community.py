import pandas as pd
from pandas import read_csv
import folium
import os
import webbrowser
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import read_csv


# read the data
crimes = read_csv('Data/Chicago_crimes_2012_to_2017.csv',error_bad_lines=False)

print('\nPreprocessing data.')
com_count = pd.DataFrame(crimes.groupby('Community Area').size().sort_values(ascending=False).rename('count').reset_index())
com = com_count
com_count['Community Area'] = com_count['Community Area'].astype('int').astype('str')
vis = os.path.join('Data/Community_Areas.json')
Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")

li1 = [[41.8810644,-87.6630450],[41.9039100,-87.6314629],[41.8948712,-87.7654014],[41.7600000,-87.5741880],[41.8990752,-87.7212930],[41.8584847,-87.7138636]]
li2 = ['near west side','near north side','austin','south shore','humboldt park','north lawndale']
#for i in range(6):
#	folium.Marker(li1[i], popup = li2[i], tooltip = li2[i]).add_to(Chicago_map)

#folium.Marker([41.878113, -87.629799], popup = '<strong>Chicago</strong>', tooltip = 'Chicago').add_to(Chicago_map)
Chicago_map.choropleth(geo_data=vis, data = com_count, columns = ['Community Area', 'count'], name='choropleth', fill_color = 'Reds', fill_opacity = '0.9', key_on = 'feature.properties.area_numbe', line_weight = '1')

folium.LayerControl().add_to(Chicago_map)
filepath = 'Community_Choropleth.html'
Chicago_map.save(filepath)
Chicago_map.save('Map.jpeg')
x = input('\nPress ENTER to view the map...')
webbrowser.open(filepath)

#2nd plot
crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv',error_bad_lines=False)
crimes = crimes.dropna()
Community_count = pd.DataFrame(crimes.groupby('Community Area').size().sort_values(ascending=False).rename('Counts').reset_index())
Community_count = Community_count.ix[:39,:]
print(Community_count)
#Dist = ['Central', 'Wentworth', 'Grand Crossing', 'South Chicago', 'Calumet', 'Gresham', 'Englewood', 'Chicago Lawn', 'Deering', 'Ogden', 'Harrison', 'Near West', 'Shakespeare', 'Austin', 'Jefferson Park', 'Albany Park', 'Near North', 'Town Hall', 'Lincoln', 'Morgan Park', 'Rogers Park', 'Grand Central']
nu = input('Enter the number of clusters required: ')
kmean = KMeans(n_clusters = int(nu))
kmean.fit(Community_count)
pr = kmean.predict(Community_count)

centers = kmean.cluster_centers_

print('Plotting graph...')
plt.figure(figsize=(12,6))
plt.scatter(Community_count['Community Area'], Community_count['Counts'], c=pr, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.xlabel('Community')
plt.ylabel('Number of Crimes')
plt.title('K-Means Clustering ')
#plt.xticks(District_count['District'].sort_values(ascending = True), Dist, rotation = 50)
plt.show()
