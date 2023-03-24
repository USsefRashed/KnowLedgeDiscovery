import pandas as pd

#This I added new dublicated fields in data set 
# lets check them using pandas
 
dataset=pd.read_csv("./student-mat.csv")

# Represents the duplicated data row which will be removed (All of them)
unkeeped=dataset.duplicated(keep=False)
print(unkeeped)

# Represents the duplicated data row which will be removed (Keep the first Remove others)
keepFirst=dataset.duplicated(keep="first")
print(keepFirst)

# Represents the duplicated data row which will be removed (Keep the Last Remove others)
keepLast=dataset.duplicated(keep="last")
print(keepLast)

#check duplicated in specific column
dupGrades=dataset.duplicated(subset=['age'])

# To drop them 
dataset.drop_duplicates()
# To drop Dublicated Data in a specific columns
dataset.drop_duplicates(subset=['col A','col B'])
# To drop Dublicated Data in a specific columns 
# and determine which duplicated row to keep
dataset.drop_duplicates(subset=['col A','col B'],keep="last")



