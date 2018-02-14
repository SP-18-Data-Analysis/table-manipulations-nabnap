# -*- coding: utf-8 -*-
import pandas as pd

#Load the data into a dataframe.
dataFrame = pd.io.parsers.read_csv('data/wine.data')

#Each columns attribute name according to: https://archive.ics.uci.edu/ml/datasets/wine
dataFrame.columns=['Class identifier', 'Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids',\
'Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline']

#For each column, output its min, max, and std.
print("************ MIN, MAX, & STD OF EACH COLUMN IN DATA FRAME ************")
for c in dataFrame.columns:
	dfc = dataFrame[c]
	print("Column: %30s ---- Min: %10.5f, Max: %10.5f, STD: %10.5f" % (c, dfc.min(), dfc.max(), dfc.std()))

print("\n")#Just giving a little space

#Apply a lambda function to the data frame to multiply each value by 6.
#No need to iterate over each column to apply the same lambda function
#when you can just apply it to the dataframe.
dataFrameAdjusted = dataFrame.apply(lambda x: x * 6) 

#Print the lambda adjusted data frame.
print("************ LAMBDA ADJUSTED DATA FRAME ************")
print(dataFrameAdjusted)
