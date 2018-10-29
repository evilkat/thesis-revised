import re
def readFile(filename):
	data_set = dict()
	
	rf = open('./dataset/'+filename,'r')
	
	for line in rf:
		line = line[:-1]
		line = line.split(" ")
		data_str = ''
		data = {}
		for i in range(0,len(line)):
			if i==0:
				data['created_at'] = line[i]
			elif i==1:
				continue
			elif i==len(line)-1:
				data['user_mentions'] = line[len(line)-1]
			elif i==len(line)-2:
				data['favorite_count'] = line[len(line)-2]
			elif i==len(line)-3:
				data['retweet_count'] = line[len(line)-3]
			else:
				data_str = data_str + line[i] + ' '
		data['text'] = data_str
		data_set[line[1]] = data 

	rf.close()
	return data_set

def getAlphaNumeric(data_text):
	#remove all words with #,$ and @
	#remove #
	clean_data = ' '
	data = data_text.split(" ")

	for dt in data:
		if re.match(r"^https:// +",dt):
			continue
		elif re.match(r"https + ",dt):
			continue
		elif re.match(r"^\\$ + ",dt):
			continue
		elif re.match(r"^# + ",dt):
			continue
		elif re.match(r"^@+ ",dt):
			continue
		elif re.match(r"bRT +",dt):
			continue
		elif re.match(r" RT +",dt):
			continue
		else:
			ndt = re.sub(r"[^A-Za-z0-9]+", '', dt)
			clean_data = clean_data + ndt + ' '    	
	return clean_data[2:len(clean_data)-1]


def checkduplicate(datadict,clean_data,created_at,user_mentions,favorite_count,retweet_count):
	interactdict = dict()
	if clean_data in datadict:
		return datadict
	else:
		interactdict["created_at"] = created_at
		interactdict["favorite_count"] = favorite_count
		interactdict["retweet_count"] = retweet_count
		interactdict["user_mentions"] = user_mentions 
		datadict[clean_data] = interactdict

		return datadict

	
def createClean(filename,datadict):
	wf = open('./datacleaning/'+filename,"a")
	for i in datadict:
		wf.write(i+' '+datadict[i]["created_at"]+' '+datadict[i]["favorite_count"]+' '+datadict[i]['retweet_count']+' '+datadict[i]['user_mentions']+'\n')
	wf.close()