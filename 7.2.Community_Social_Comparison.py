print('Including required libraries.')
print('Importing CSV file into dataframe.')

import pandas as pd
from pandas import read_csv
import folium
import os
import webbrowser

se = read_csv('Socioeconomic.csv')
se = se.loc[:, ['PERCENT AGED 16+ UNEMPLOYED', 'COMMUNITY AREA NAME', 'Community Area Number', 'PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA', 'PER CAPITA INCOME ']]
i = se[(se['COMMUNITY AREA NAME'] == 'CHICAGO')].index
se = se.drop(i)
se['Community Area Number'] = se['Community Area Number'].astype('int').astype('str')
vis = 'Community_Areas.geojson'


m1 = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")
m1.choropleth(geo_data=vis, data = se, columns = ['Community Area Number', 'PERCENT AGED 16+ UNEMPLOYED'], fill_color = 'YlGn', fill_opacity = '0.9', key_on = 'feature.properties.area_num_1')
folium.LayerControl().add_to(m1)
filepath = 'Unemployment_rate.html'
m1.save(filepath)
#webbrowser.open('Literacy_rate.html')

m2 = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")
m2.choropleth(geo_data=vis, data = se, columns = ['Community Area Number', 'PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA'], fill_color = 'YlGn', fill_opacity = '0.9', key_on = 'feature.properties.area_num_1')
folium.LayerControl().add_to(m2)
filepath = 'Literacy_rate.html'
m2.save(filepath)
#webbrowser.open('Literacy_rate.html')

print(se)
m3 = folium.Map(location = [41.878113, -87.629799], zoom_start = 10, tiles = "cartodbpositron")
m3.choropleth(geo_data=vis, data = se, columns = ['Community Area Number', 'PER CAPITA INCOME '], fill_color = 'YlGn', fill_opacity = '0.9', key_on = 'feature.properties.area_num_1')
folium.LayerControl().add_to(m3)
filepath = 'Per_capita_income.html'
m3.save(filepath)

x = input('END')