print('Including headers.')
print('Importing CSV file into DataFrame.')

import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv', index_col='Date')

crime_count = pd.DataFrame(crimes.groupby('Primary Type').size().sort_values(ascending=False).rename('counts').reset_index())
print(crime_count)
print('\nPlotting graph.')
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6, 15))

sns.set_color_codes("pastel")
sns.barplot(x="counts", y="Primary Type", data=crime_count.iloc[:10, :], label="Total", palette = "Reds_d")
ax.set(ylabel="Number of crimes commited", xlabel="Crimes")
sns.despine(left=True, bottom=True)
x = input('\nPress ENTER to view graph.')
plt.show()

crimes.index = pd.to_datetime(crimes.index)
print('Plotting graph.')
sns.set(style="darkgrid")
cr = pd.DataFrame(crimes[crimes['Primary Type'].isin(['THEFT','BATTERY', 'CRIMINAL DAMAGE', 'NARCOTICS', 'ASSAULT'])]['Primary Type'])
grouper = cr.groupby([pd.TimeGrouper('M'), 'Primary Type'])
cr2 = grouper['Primary Type'].count().unstack()
cr2.plot()
plt.title("Top five type of crimes")
print('Press ENTER to view graph.')
plt.show()
x = input('\nPress any key to exit.')

