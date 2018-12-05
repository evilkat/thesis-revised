import pymongo
from pymongo import MongoClient
import pprint
import json

companylist=['AAPL','AMZN','FB','GOOG','JCP','MSFT','NFLX','TSLA']

def printToFile(record,company,count):
	print(count)
	fw = open('datavalues/'+company+record['date']+'.csv','a')
	fw.write(record['message']+','+record['retweet_count']+','+record['engage_count']+','+record['favorite_count']+'\n')
	
	fw.close()
	#print(data)
	count = count + 1
	return count 

def getDates(company,client,db,collection):
	dates = list()
	try:
		for record in collection.distinct('date'):
			dates.append(record)

		return dates
	except BaseException as e:
		print(e)
		print("failed getting of date")

def getRecord(company):
	try:
		client = MongoClient("localhost",27017)
		db = client['thesis']
		collection = db[company]
		dates=getDates(company,client,db,collection)
		#print('Total Record for the collection: '+str(collection.count()))
		for date in dates:
			count = 1
			if date in ['2018-07-26','2018-07-27','2018-07-30','2018-08-01','2018-08-02','2018-08-06','2018-08-07','2018-08-08','2018-08-09','2018-08-10','2018-08-13','2018-08-14','2018-08-15','2018-08-16']:
				continue
			else:
				for record in collection.find({'date':date}):
					count=printToFile(record,company,count)
	except BaseException as e:
		print(e)
		print("Failed fetch")

#for name in companylist:
getRecord('AAPL')