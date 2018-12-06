import pandas as pd

def readData(filename):
	
	return pd.read_csv('../datavalues/AAPL2018-07-26.csv',sep=',',header=None)

data = readData('../datavalues/AAPL2018-07-26.csv')

data = data.drop_duplicates()

for i in range(0,len(data[0])):
	print(data[0][i])

