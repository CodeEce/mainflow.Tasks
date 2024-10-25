import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
data = pd.read_csv('C:\\Users\\HP\\Desktop\\Main flow\\householdtask3.csv')
data.head(10)

# scatter plot with year against own
plt.scatter(data['year'],data['own'])
# Adding title to the plot
plt.title('Scatter Plot')
# setting the x and y labels
plt.xlabel('Year')
plt.ylabel('Own')
plt.show()
# Bar Chart with year against own
plt.bar(data['year'],data['own'])
plt.title('Bar Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()
# line chart with year against own
plt.plot(data['year'],data['own'])
plt.title('Line Chart')
plt.xlabel('year')
plt.ylabel('own')
plt.show()
# HISTOGRAM
plt.hist(data['income'])
plt.title('Histogram')
plt.show()





