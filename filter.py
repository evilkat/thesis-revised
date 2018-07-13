#cleans the passed json object
import os
import preprocessor as p

def clean(tweet):
	
	#for create at
	tweet_create=tweet['created_at'].replace(' ','')
	print(tweet_create)

	#for id
	tweet_id = str(tweet['id'])

	#for textvalue
	tweet_text = str(tweet['text'].encode('ascii','ignore'))
	#tweet_text=p.clean(tweet_text)
	print(tweet_text)

	#for retweet_count
	tweet_rc = str(tweet['retweet_count']) 

	#for favorite_count
	tweet_fc = str(tweet['favorite_count'])

	#for user_mentions 
	tweet_engage=len(tweet['entities']['user_mentions'])
	tweet_engage = str(tweet_engage)

	#format data
	#created_at,id,text,tweet_rc,tweet_fc,tweet_engage

	tweet_string = str(tweet_create) + ' ' + str(tweet_id) + ' ' + str(tweet_text) + ' ' + tweet_rc + ' ' + tweet_fc + ' ' + tweet_engage + '\n'
	return tweet_string 

#cleans the text for insert in database
def formatText(textlist):
	newtext = ' '
	for line in textlist:
		line = line.strip("'")
		#line = line.strip("RT:")
		line = line.strip('"')
		newtext = newtext + ' ' + line
	newtext = newtext[4:]
	#print(newtext)
	newtext = p.clean(newtext)
	print(newtext)


#this function is for the dictionary for eliminating duplicate tweets and RTs	
#def formatData(data):

def readFile(filename):
	rf = open('./dataset/'+filename,'r')
	data = list()
	for line in rf:
		line=line[:-1]
		data = line.split(" ")
		textlist = data[2:-3]
		formatText(textlist)


def cleaningFile():
	arr = os.listdir('./dataset/')
	print(arr)
	for file in arr:
		readFile(file)
		break			#remove this if cleaning is done









