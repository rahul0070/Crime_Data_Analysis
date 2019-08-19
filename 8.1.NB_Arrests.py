print('Including headers.')
print('Importing CSV file into DataFrame.')

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
crimes = read_csv('Chicago_Crimes_2012_to_2017.csv')
crimes = crimes.dropna()
df = crimes.loc[:10000,['Domestic', 'Location Description', 'Arrest', 'District', 'Primary Type']]

ix = ['THEFT', 'BATTERY', 'ASSAULT', 'HOMICIDE', 'NARCOTICS', 'KIDNAPPING', 'HUMAN TRAFFICKING', 'PROSTITUTION']
lx = ['STREET', 'RESIDENCE', 'APARTMENT', 'SIDEWALK', 'OTHER']

df = df.loc[df['Primary Type'].isin(ix), :]
df = df.loc[df['Location Description'].isin(lx), :]

df['Primary Type'] = le.fit_transform(df['Primary Type'].tolist())
d1 = dict(zip(le.classes_, le.transform(le.classes_)))

df['Arrest'] = le.fit_transform(df['Arrest'].tolist())
d2 = dict(zip(le.classes_, le.transform(le.classes_)))

df['Domestic'] = le.fit_transform(df['Domestic'].tolist())
d3 = dict(zip(le.classes_, le.transform(le.classes_)))

df['Location Description'] = le.fit_transform(df['Location Description'].tolist())
d4 = dict(zip(le.classes_, le.transform(le.classes_)))


pr_data = df[['Primary Type', 'Location Description', 'Domestic']]
pr_target = df[['Arrest']]

gnb = GaussianNB()
y_pred = gnb.fit(pr_data, pr_target).predict(pr_data)

print('Primary Type: ', d1)
print('Domestic: ', d3)
print('Location: ', d4)
print('Arrest: ', d2)

print('\nAccuracy: ', gnb.score(pr_data, pr_target)*100, '%')

a = input('Enter Primary Type:')
b = input('Enter Location:')
c = input('Enter Domestic:')

re = gnb.predict([[int(a), int(b), int(c)]])
if re == [0]:
	print('Result: FALSE')
else:
	print('Result: TRUE')


x = input('COMPLETED')
