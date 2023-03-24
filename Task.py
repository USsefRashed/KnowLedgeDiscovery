import pandas as pd

#This is the first task of knowledge discovery subject

# in this branch I will remove some object's properties
# To deal with missing values
 


#Reading dataset File 
dataset=pd.read_csv("./student-mat.csv")
missing=pd.DataFrame({'Missed Count':dataset.isnull().sum()})
# To drop them (Ignoring rows which contains null values)
dataset.dropna()
# To Fill them (Fill rows which contains null values with the median values)
dataset.fillna(dataset['age'].median())

print(missing)
