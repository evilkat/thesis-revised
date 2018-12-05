from textblob import TextBlob
import pandas as pd

def readData(filename):
	data = pd.read_csv(filename,sep=',')
	return data

data = readData('../datavalues/AAPL2018-07-26.csv')

#print(data['msg'])

val = data['msg']


for i in range(1,len(val)):
	text_senti = TextBlob(val.iloc[i])
	if text_senti.sentiment.polarity == 0 or text_senti.sentiment.subjectivity == 0:
		continue
	else:
		print(val.iloc[i])
		print(text_senti.sentiment)