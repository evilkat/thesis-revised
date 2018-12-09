from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
import computeMean



def writeData(date,mean_sentiment,neg,pos):
	fw = open('sentimentMSFT.csv','a')
	fw.write(date+','+str(mean_sentiment)+','+str(neg)+','+str(pos)+'\n')
	fw.close()
#july to august
listdate = ['2018-07-26','2018-07-27','2018-07-30','2018-08-01','2018-08-02','2018-08-06','2018-08-07','2018-08-08','2018-08-09','2018-08-10','2018-08-13','2018-08-14','2018-08-15','2018-08-20','2018-08-23','2018-08-28','2018-08-30']
#listdate = ['2018-09-03','2018-09-04','2018-09-05','2018-09-06','2018-09-07','2018-09-10','2018-09-11','2018-09-12','2018-09-13','2018-09-17','2018-09-18','2018-09-19','2018-09-20','2018-09-21','2018-09-24','2018-09-25','2018-09-26','2018-09-27','2018-09-29',]
#listdate = ['2018-10-01','2018-10-02','2018-10-03','2018-10-04','2018-10-05','2018-10-08','2018-10-09','2018-10-10','2018-10-11','2018-10-12','2018-10-15','2018-10-16','2018-10-17','2018-10-18','2018-10-19','2018-10-22','2018-10-23','2018-10-24','2018-10-29','2018-10-30',]
#listdate = ['2018-11-05','2018-11-06','2018-11-13','2018-11-14','2018-11-15','2018-11-19','2018-11-21']
client = MongoClient("localhost",27017)
db = client["thesis"]
collection = db['MSFT']


for date in listdate:
	analyser = SentimentIntensityAnalyzer()
	data = pd.DataFrame(list(collection.find({'date':date})))
	data = data.drop_duplicates()
	data['message'] = data['message'].astype('str')
	data['retweet_count'] = data['retweet_count'].replace(r'\s+',np.nan,regex=True)
	data['engage_count'] = data['engage_count'].replace(r'\s+',np.nan,regex=True)
	data['favorite_count'] = data['favorite_count'].replace(r'\s+',np.nan,regex=True)
	data = data.dropna()
	sentiment_scores = list()
	for line in data['message']:
		text_sentiment = analyser.polarity_scores(line)
		sentiment_scores.append(text_sentiment['compound'])

	data['sentiment'] = sentiment_scores
	data = data.drop(data[(data['sentiment']==0)].index)
	
	mean_sentiment,neg,pos=computeMean.computeMean(data,date)
	writeData(date,mean_sentiment,neg,pos)
	print('printing to file '+date)
	data.to_csv('withsentiment/MSFT'+date+'.csv',index=False)
