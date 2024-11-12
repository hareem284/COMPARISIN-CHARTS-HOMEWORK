#importing matplotlib 
import matplotlib.pyplot as plt
#importing pandas to read csv file
import pandas as pd
#importing seaborn 
import seaborn as sns
#reading csv file
rcsv=pd.read_csv("fuel.csv")
print(rcsv.info())
rcsv.isnull().any()
#print(rcsv.groupby(['Fuel Type']).mean())
#making a count plot
sns.countplot(rcsv,x='Vehicle Class',palette='winter')
plt.show()
# making a bar plot
plt.bar(rcsv['Fuel Type'],rcsv['CO2 emissions'],color='maroon')
plt.show()