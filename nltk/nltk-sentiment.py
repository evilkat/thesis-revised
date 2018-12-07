from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

#july to august
listdate = ['2018-07-26','2018-07-27','2018-07-30','2018-08-01','2018-08-02','2018-08-06','2018-08-07','2018-08-08','2018-08-09','2018-08-10','2018-08-13','2018-08-14','2018-08-15','2018-08-20','2018-08-23','2018-08-28','2018-08-30']
client = MongoClient("localhost",27017)
db = client["thesis"]
collection = db['AAPL']


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
	print('printing to file '+date)
	data.to_csv('withsentiment/AAPL'+date+'.csv',index=False)
