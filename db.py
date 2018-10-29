import pymongo
from pymongo import MongoClient


def insertData(sentence_dictionary,company):
	try:
		client = MongoClient("localhost",27017)
		db = client['thesis']
		collection = db[company]
		for message in sentence_dictionary:
			collection.insert([{'message':message,'retweet_count':sentence_dictionary[message][0],'favorite_count':sentence_dictionary[message][1],'engage_count':sentence_dictionary[message][2],'date':sentence_dictionary[message][3]}])
	except BaseException as e:
		print(e)
		print("Failed insert")
