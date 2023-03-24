import pandas as pd
import matplotlib.pyplot as pt
#In This is branch I will add noisy data in my data set and represent it graphically 

at=['age','G1']

#Reading dataset File 
dataset=pd.read_csv("./student-mat.csv")

dataset[at].boxplot()
pt.title("Data")
pt.show()

