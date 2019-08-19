import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn.cluster import KMeans

crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv',error_bad_lines=False)

crimes.index = pd.to_datetime(crimes.index)
crimes.Date = pd.to_datetime(crimes.Date, format = '%m/%d/%Y %I:%M:%S %p')
crimes.index = pd.DatetimeIndex(crimes.Date)

#1st plot
arrest_yearly = crimes[crimes['Year'] != 2017]['Arrest']
print('Plotting graphs...')
plt.subplot()
arrest_yearly.resample('A').sum().plot()
plt.title('Number of Crimes each year')
plt.show()
arrest_yearly.resample('M').sum().plot()
plt.title('Number of Crimes each year')
plt.show()

#2nd plot
crimes.groupby([crimes.index.month]).size().plot.bar()
plt.title('Total no.of crimes Per Month')
plt.xlabel('Month')
plt.ylabel('Number of Crimes commited')
plt.show()

