print('Finiding the best locality to live in the city:')
from gtts import gTTS 
from playsound import playsound
import threading
def audio0():
	playsound('Audio/Module2_0.mp3')
t0 = threading.Thread(target=audio0)
t0.start()


print('\nImporting required libraries...')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
import os
import webbrowser
import folium
import time
import json
import altair as alt
from vega_datasets import data


gTTS(text='Press enter to view the result', lang='en', slow=False).save('Audio/output.mp3')
def audio1():
	playsound('Audio/input.mp3')

def audio2():
	playsound('Audio/output_2.mp3')

def audio3():
	playsound('Audio/output_2.mp3')
	playsound('Audio/output.mp3')

def audio4():
	playsound('Audio/Module2_1.mp3')

def audio5():
	playsound('Audio/Module2_2.mp3')

def audio6():
	playsound('Audio/Module2_3.mp3')

def audio7():
	playsound('Audio/Module2_4.mp3')


print('Importing Dataset...')
crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv')
vis = 'Data/Community_Areas.json'
crimes = crimes.dropna()

com_count = pd.DataFrame(crimes.groupby('Community Area').size().sort_values(ascending=False).rename('count').reset_index())
com_count['Community Area'] = com_count['Community Area'].astype('int').astype('str')
c1 = com_count.tail(10)
print(c1)
lc1 = c1['Community Area'].tolist()
Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")

#li1 = [[41.8810644,-87.6630450],[41.9039100,-87.6314629],[41.8948712,-87.7654014],[41.7600000,-87.5741880],[41.8990752,-87.7212930],[41.8584847,-87.7138636]]
#li2 = ['near west side','near north side','austin','south shore','humboldt park','north lawndale']
#for i in range(6):
#	folium.Marker(li1[i], popup = li2[i], tooltip = li2[i]).add_to(Chicago_map)

#folium.Marker([41.878113, -87.629799], popup = '<strong>Chicago</strong>', tooltip = 'Chicago').add_to(Chicago_map)
Chicago_map.choropleth(geo_data=vis, data = com_count, columns = ['Community Area', 'count'], name='choropleth', fill_color = 'Reds', fill_opacity = '0.9', key_on = 'feature.properties.area_numbe', line_weight = '1')

folium.LayerControl().add_to(Chicago_map)
filepath = 'Community_Choropleth.html'
Chicago_map.save(filepath)
t2 = threading.Thread(target=audio3)
t2.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)
tx1 = threading.Thread(target=audio4)
tx1.start()

se = read_csv('Data/Socioeconomic.csv')
se = se.loc[:, ['COMMUNITY AREA NAME', 'Community Area Number', 'HARDSHIP INDEX']]
i = se[(se['COMMUNITY AREA NAME'] == 'CHICAGO')].index
se = se.drop(i)
se = se.sort_values(by = ['HARDSHIP INDEX'], ascending=False).reset_index()
c2 = se.ix[:,['Community Area Number', 'HARDSHIP INDEX']]
c2 = c2.tail(10)
lc2 = c2['Community Area Number'].tolist()
print(c2)

veg = alt.Chart(se.reset_index()).mark_line().encode(
    x='Community Area Number:T',
    y='HARDSHIP INDEX:Q'
)
veg.save('veg.json')

se['Community Area Number'] = se['Community Area Number'].astype('int').astype('str')
m = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")

m.choropleth(geo_data=vis, data = se, columns = ['Community Area Number', 'HARDSHIP INDEX'], fill_color = 'YlGn', key_on = 'feature.properties.area_num_1')
folium.LayerControl().add_to(m)

folium.Marker(
    location=[41.878113, -87.629799],
    popup=folium.Popup(max_width=450).add_child(
        folium.Vega(json.load(open('veg.json')), width=450, height=250))
).add_to(m)

m.save('social_rate.html')
t3 = threading.Thread(target=audio2)
tx1.join()
t3.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open('social_rate.html')
tx2 = threading.Thread(target=audio5)
tx2.start()


pc = read_csv('Data/Chicago_Department_of_Public_Health_Clinic_Locations.csv')

Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")

la = pc['Latitude'].tolist()
lo = pc['Longitude'].tolist()
li2 = pc['Site Name'].tolist()
for i in range(24):
	folium.Marker([la[i], lo[i]], popup = li2[i], tooltip = li2[i]).add_to(Chicago_map)

Chicago_map.choropleth(geo_data=vis, data = com_count, columns = ['Community Area', 'count'], name='choropleth', fill_color = 'OrRd', fill_opacity = '0.4', key_on = 'feature.properties.area_numbe', line_weight = '1')
folium.LayerControl().add_to(Chicago_map)
filepath = 'Clinic_Choropleth.html'
Chicago_map.save(filepath)
t2 = threading.Thread(target=audio2)
tx2.join()
t2.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)
tx3 = threading.Thread(target=audio6)
tx3.start()


house = read_csv('Data/Affordable_Rental_Housing_Developments.csv')
crh = pd.DataFrame(house.groupby('Community Area Number').size().sort_values(ascending=False).rename('count').reset_index())
crh['Community Area Number'] = crh['Community Area Number'].astype('int').astype('str')
c3 = crh.ix[:10,:]
print(c3)
crh.to_csv('check.csv')
crh.loc[crh['count'] == 0, ['count']] = '1'
Chicago_map = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "CARTODBPOSITRON")
Chicago_map.choropleth(geo_data=vis, data = crh, columns = ['Community Area Number', 'count'], name='choropleth', fill_color = 'YlGnBu', fill_opacity = '0.9', key_on = 'feature.properties.area_numbe', line_weight = '1')
folium.LayerControl().add_to(Chicago_map)
filepath = 'Housing_Choropleth.html'
Chicago_map.save(filepath)
tx3.join()
t4 = threading.Thread(target=audio2)
t4.start()
x = input('\nPress ENTER to view the map.')
webbrowser.open(filepath)
tx4 = threading.Thread(target=audio7)
tx4.start()

print('END')

lf = []
l0 = []
lc1.remove('0')
for i in lc1:
	if int(i) in lc2:
		lf.append(int(i))

for i in lc2:
	if int(i) in lc1:
		lf.append(int(i))


print(lf)

lc1.reverse()
lc2.reverse()

print(lc1)
print(lc2)

for i in range(5):
	lf.append(int(lc1[i]))

for i in range(5):
	lf.append(int(lc2[i]))

res = [] 
[res.append(x) for x in lf if x not in res]
print(res)

pc1 = pd.DataFrame(pc.groupby('Community').size().sort_values(ascending=False).rename('count').reset_index())
print(pc1)

x = input('END')
