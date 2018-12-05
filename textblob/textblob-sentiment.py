from textblob import TextBlob
import pandas as pd
import numpy as np

def readData(filename):
	data = pd.read_csv(filename,sep=',')
	return data

data = readData('../datavalues/AAPL2018-07-26.csv')

#print(data['msg'])

val = data['msg']
count = 1
for i in range(1,len(val)):
	text_senti = TextBlob(str(val.iloc[i]))
	if text_senti.sentiment.polarity == 0 or text_senti.sentiment.subjectivity == 0:
		continue
	else:
		print(count)
		fw = open('withsentiment/AAPL2018-07-26.csv','a')
		#print(text_senti.sentiment.polarity)
		#print(val.iloc[i],data['rc'].iloc[i],data['ec'].iloc[i],data['fc'].iloc[i])
		fw.write(val.iloc[i]+','+str(data['rc'].iloc[i])+','+str(data['ec'].iloc[i])+','+str(data['fc'].iloc[i])+','+str(text_senti.sentiment.polarity)+'\n')
		fw.close()
		count = count + 1