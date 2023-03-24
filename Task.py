import pandas as pd

#This is the first task of knowledge discovery subject

# In this task I work on data for students grades in
# maths exam to perform the data preprocessing and display the noisy ...etc 


#Reading dataset File 
dataset=pd.read_csv("./student-mat.csv")

#Get first 5 objects of the dataset
print(dataset.head())

#Get the count of the rows and attributes
print(dataset.shape)

#Get the data types of columns
print(dataset.dtypes)

# Get the information data set
print(dataset.info())

# Get the information data set
print(dataset.describe())

# to see duplicated data I added it manually in branch with name Dublicated-Dealing

