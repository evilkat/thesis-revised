import re
def readFile(filename):
	data_set = dict()
	rf = open(filename,'r')
	
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
		elif re.match(r"^\\$ +",dt):
			continue
		elif re.match(r"^# +",dt):
			continue
		elif re.match(r"^@+",dt):
			continue
		elif re.match(r"bRT",dt):
			continue
		else:
			ndt = re.sub(r"[^A-Za-z0-9]+", '', dt)
			clean_data = clean_data + ndt + ' '    	
	print(clean_data)
	
#print(ftext)

		#ftext = " ".join (filter(lambda x:x[0]!='$',ftext.split()))
#print(ftext)

		#re.sub(r"\\\n+",'',ftext)
#print(ftext)

		#re.sub(r"\\\n\n+",'',ftext)
	#print(ftext)

	


	'''
	#remove @
	ftext = " ".join (filter(lambda x:x[0]!='$',ftext.split()))
	print(ftext)
	
	#remove $
	
	ftext = re.match(r"(\w+)(\w+)",ftext)
	print(ftext)
	
	'''




'''
def cleanDataset(data_set):
	clean_data = dict()
	for line in data_set:
		line = line.split(" ")
		clean_data['created_at'] = line[0]
		clean_data['id'] = line[1]
		clean_data['retweet_count'] = line[-3]
		clean_data['favorite_count'] = line[-2]
		clean_data['user_mentions'] = line[-1]
		print(clean_data)
	print(data_set)

cleanDataset(readFile('sample.txt'))
'''
data_set=readFile('sample.txt')
for i in data_set:
	print(getAlphaNumeric(data_set[i]['text']))