# Data Manipulation with Pandas
import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv('C:\\Users\\HP\\Desktop\\Main flow\\01.Data Cleaning and Preprocessing.csv')
type(data)
data.info()
data.describe()
data = data.drop_duplicates()
print(data)
data.isnull()
data.isnull().sum()
data.notnull()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
print(data2)
data3 = data.fillna(method='pad')
print(data3)
data4 = data.fillna(method='bfill')
print(data4)

var = data2.columns
print(var)
data2.drop(['Observation'], axis=1,inplace=True)
print(data2.columns)
q1 = data2.quantile(0.25)
q3 = data2.quantile(0.75)
IQR = q3-q1
print(IQR)
data2 = data2[~((data2<(q1-1.5*IQR))|(data2>(q3+1.5*IQR))).any(axis=1)]
print(data2)
data.describe()