from textblob import TextBlob
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client["thesis"]
collection = db['AAPL']
date = '2018-07-26'
data = pd.DataFrame(list(collection.find({'date':date})))

data = data.drop_duplicates()
data['message'] = data['message'].astype('str')
data['retweet_count'] = data['retweet_count'].replace(r'\s+',np.nan,regex=True)
data['engage_count'] = data['engage_count'].replace(r'\s+',np.nan,regex=True)
data['favorite_count'] = data['favorite_count'].replace(r'\s+',np.nan,regex=True)
data = data.dropna()
sentiment_scores = list()
for line in data['message']:
	text_sentiment = TextBlob(line)
	sentiment_scores.append(text_sentiment.polarity)
data['sentiment'] = sentiment_scores
data = data.drop(data[(data['sentiment']==0)].index)
print(data.head())
print(data.tail())
