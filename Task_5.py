import matplotlib
import matplotlib_inline
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data =pd.read_csv('C:\\Users\\HP\\Desktop\\Main flow\\heart.csv')
data.head()
data.tail()
data.info()
data.describe()
print("Original shape:", data.shape)
data = data.drop_duplicates()
print("After removing duplicates:", data.shape)
data.isnull().sum()

data.hist(bins=50,grid=False,figsize=(20,15))
plt.show()

data.describe()

# 1.What is the average age of patients with and without heart disease?
average_age = data.groupby('target')['age'].mean()
average_age.plot(kind='bar', color=['skyblue', 'salmon'])
plt.title('Average Age of Patients with and without Heart Disease')
plt.xlabel('Heart Disease (0 = No, 1 = Yes)')
plt.ylabel('Average Age')
plt.xticks(rotation=0)
plt.show()

# 2. What is the distribution of cholesterol levels for patients with heart disease versus those without?
data[data['target'] == 1]['chol'].hist(alpha=0.5, label='Heart Disease', bins=50, grid =False)
data[data['target'] == 0]['chol'].hist(alpha=0.5, label='No Heart Disease', bins=50, grid =False)
plt.legend()
plt.xlabel('Cholesterol Levels')
plt.ylabel('Frequency')
plt.title('Cholesterol Levels Distribution by Heart Disease Status')
plt.show()

# 3.What is the relationship between maximum heart rate (thalach) and age for patients with and without heart disease?
plt.figure(figsize=(10, 6))
plt.scatter(data[data['target'] == 1]['age'], data[data['target'] == 1]['thalach'], color='salmon', label='Heart Disease', alpha=0.6)
plt.scatter(data[data['target'] == 0]['age'], data[data['target'] == 0]['thalach'], color='skyblue', label='No Heart Disease', alpha=0.6)
plt.title('Age vs. Maximum Heart Rate (thalach)')
plt.xlabel('Age')
plt.ylabel('Maximum Heart Rate (thalach)')
plt.legend()
plt.show()

# 4. What is the distribution of resting blood pressure (trestbps) for patients with and without heart disease?
plt.figure(figsize=(10, 6))
data.boxplot(column='trestbps', by='target', grid=False, patch_artist=True, medianprops=dict(color="black"))
plt.title('Resting Blood Pressure Distribution by Heart Disease Status')
plt.suptitle('')  # Removes the automatic title from Pandas
plt.xlabel('Heart Disease (0 = No, 1 = Yes)')
plt.ylabel('Resting Blood Pressure (trestbps)')
plt.show()

# 5.  What is the distribution of resting blood pressure (trestbps) for patients with and without heart disease?
plt.figure(figsize=(10, 6))
data.boxplot(column='trestbps', by='target', grid=False, patch_artist=True, medianprops=dict(color="black"))
plt.title('Resting Blood Pressure Distribution by Heart Disease Status')
plt.suptitle('')  # Removes the automatic title from Pandas
plt.xlabel('Heart Disease (0 = No, 1 = Yes)')
plt.ylabel('Resting Blood Pressure (trestbps)')
plt.show()

# 6. How does the depression induced by exercise (oldpeak) vary with different slopes of the peak exercise ST segment?
plt.figure(figsize=(10, 6))
sns.violinplot(x='slope', y='oldpeak', hue='target', data=data, split=True, palette='Set2')
plt.title('Distribution of Oldpeak by Slope of ST Segment')
plt.xlabel('Slope of Peak Exercise ST Segment')
plt.ylabel('Oldpeak (Depression induced by Exercise)')
plt.legend(title='Heart Disease')
plt.show()

# 7. How many patients have different types of chest pain and heart disease?
chest_pain_heart_disease = data.groupby('cp')['target'].value_counts().unstack()

chest_pain_heart_disease.plot(kind='bar', stacked=True, color=['skyblue', 'salmon'], figsize=(10, 6))
plt.title('Chest Pain Type and Heart Disease')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.legend(['No Heart Disease', 'Heart Disease'])
plt.xticks(rotation=0)
plt.show()
sns.displot(x='age',data=data,bins=30,kde=True)
sns.displot(x='thalach',data=data,bins=30,kde=True,color='purple')
plt.show()















