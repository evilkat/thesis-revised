import tweepy
import jsonpickle
import os

API_KEY = 'DHjYxfSwthP3CDCsoi2NAD1LD'
API_SECRET = 'gXjx7X9gqpB6EHnFtY87zXqzoUa5ar4B5CjpGv11Jy96ocSCYW'

auth = tweepy.AppAuthHandler(API_KEY,API_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

if (not api):
	print("Can't Authenticate")
	sys.exit(-1)
else:

