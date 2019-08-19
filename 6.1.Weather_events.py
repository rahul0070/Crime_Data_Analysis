print('Importing CSV file into dataframe...')
import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt

crimes = read_csv('Data/CrimeDataset.csv', index_col='Date')
print('Data type: ', type(crimes))

print('Removing NULL values...')
symbol = (())

print('\nFilling empty values...')
crimes['Events'].fillna('Clear', inplace = True)

event_count = pd.DataFrame(crimes.groupby('Events').size().sort_values(ascending=False).rename('count').reset_index())
print(event_count)
print('\nPlotting the graph...')
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("dark")
sns.barplot(x="count", y="Events", data=event_count.iloc[:10, :], label="Total", palette = 'Blues_d')

ax.set(ylabel="Weather", xlabel="Crimes")
sns.despine(left=True, bottom=True)
plt.show()

print('\nFrom the plotted graph we can see that most number of criminal activities happened when the weather was clear. Suggesting that weather had a sizable impact over the crime frequency. To analyse further, we will now look into the data only considering crimes which have taken when the weather was not serene.')
x = input('\n Press any key to continue:')
print('\nWithout considering the most common weather condition')

print('\nImporting CSV file into dataframe...')
crimes2 = read_csv('Data/CrimeDataset.csv', index_col='Date')
print('Data type: ', type(crimes2))

print('Removing NULL values...')
symbol = (())
event_count2 = pd.DataFrame(crimes2.groupby('Events').size().sort_values(ascending=False).rename('count').reset_index())

print('\nPlotting the second graph...')
sns.set(style="darkgrid")
f, ax = plt.subplots(figsize=(6, 15))
sns.set_color_codes("dark")
sns.barplot(x="count", y="Events", data=event_count2.iloc[:10, :], label="Total", palette = 'Blues_d')

ax.set(ylabel="weather", xlabel="Crimes")
sns.despine(left=True, bottom=True)
plt.show()

print('\n We see from the above graph that negating crimes which occured during serene weather condition, The next most highly probable weather condition for a crime to take place would be "Rain" and the least probable weather for a crime to take place would be weather events such as Fog with Rain and snow.')
x = input('\n*** END ***')

