import pymongo
from pymongo import MongoClient
import pprint

companylist=['AAPL','AMZN','FB','GOOG','JCP','MSFT','NFLX','TSLA']

def getRecord(company):
	try:
		client = MongoClient("localhost",27017)
		db = client['thesis']
		collection = db[company]
		print('Total Record for the collection: '+str(collection.count()))
		for record in collection.distinct("date"):
			print(record)
	except BaseException as e:
		print(e)
		print("Failed fetch")

#for name in companylist:
getRecord('AAPL')