import filter_data
import os
import cleaning
import db
#filter.readFile('2018-07-26$AAPL')

files = os.listdir('./dataset/')
sentence_dictionary = dict()
cnt = 1
for file in files:
	#print(file)
	sentence_dictionary=cleaning.readFile(file)
	date,company = file.split('$')
	db.insertData(sentence_dictionary,company)	
	print(len(sentence_dictionary))
	print(str(cnt) +" of " + str(len(files)))
	cnt = cnt + 1