import tweepy
import jsonpickle
import os
import datetime
import json
import filter
import sys

API_KEY = 'DHjYxfSwthP3CDCsoi2NAD1LD'
API_SECRET = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'
tweets_per_query = 100
max_tweets = 10000000
max_id = -1
sinceId = None

def cleanTweets(tweet,f):
	tweet_data = json.loads(tweet)

	tweet_string=filter.clean(tweet_data)

	try:
		f.write(tweet_string)
	except UnicodeError:
		print("UnicodeError")
def getTweets(filename,search_query):
	fname = './dataset/'+datetime.datetime.today().strftime('%Y-%m-%d') + search_query
	tweet_count = 0
	print(fname)
	print("Downloading max {0} tweets".format(max_tweets))
	max_id = -1
	count_new = 0
	with open(fname,'a') as f:
		while tweet_count < max_tweets:
			try:
				if max_id <=0:
					if not sinceId:
						new_tweets = api.search(q=search_query,count=tweets_per_query,lang='en')

					else:
						new_tweets = api.search(q=search_query,count=tweets_per_query,since_id=sinceId,lang='en')
				
				else:
					if not sinceId:
						new_tweets = api.search(q=search_query,count=tweets_per_query,max_id=str(max_id-1),lang='en')
					else:
						new_tweets = api.search(q=search_query,count=tweets_per_query,max_id=str(max_id-1),since_id=sinceI,lang='en')
				
				if not new_tweets:
					print("No more tweets found")
					continue
						
					#f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
				else:
					for i in range(0, len(new_tweets)):
						tweet_value = jsonpickle.encode(new_tweets[i]._json)
						cleanTweets(tweet_value,f)	
					
					tweet_count += len(new_tweets)
					#print("downloaded {0} tweets".format(tweet_count))
				if len(new_tweets) != 0:
					#print('new_tweets[0] ',new_tweets[0].id)
					max_id = new_tweets[-1].id
				else:
					max_id = -1
			except tweepy.TweepError as e:
				#print ('some error: '+str(e))
				break
	print("Downloaded {0} tweets, Saved to {1}".format(tweet_count,fname))

#CONSTANTS


auth = tweepy.AppAuthHandler(API_KEY,API_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


if (not api):
	print("Can't Authenticate")
	sys.exit(-1)
else:
	getTweets("sample",sys.argv[1])

