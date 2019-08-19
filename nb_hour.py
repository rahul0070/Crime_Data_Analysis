import pandas as pd
from pandas import read_csv
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn import preprocessing

le = preprocessing.LabelEncoder()

print('IMPLEMENTING NAIVE BAYES CLASSIFIER TO PREDICT THE RESULT OF ARREST IN A GIVEN SITUATION')

cluster_map = read_csv('Data/cluster.csv')
l0 = []
l1 = []
l2 = []
li1 = cluster_map['cluster'].tolist()
li2 = cluster_map['data_index'].tolist()

crimes = read_csv('Data/Chicago_Crimes_2012_to_2017.csv')
crimes = crimes.dropna()
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


for i in l0:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'a'

for i in l1:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'b'

for i in l2:
	crimes.loc[crimes['Hour'] == i, ['Value']] = 'c'

cr_a = crimes.loc[crimes['Value'] == 'a', :]
cr_b = crimes.loc[crimes['Value'] == 'b', :]
cr_c = crimes.loc[crimes['Value'] == 'c', :]

df = cr_a.loc[:,['Arrest','Primary Type', 'Value']]
print(df)

