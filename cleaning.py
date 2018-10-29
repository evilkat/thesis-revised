import re
sentence_dictionary = dict()
def checkDuplicate(sentence,rc,fc,ec,date):

	content = list()
	content.append(rc)
	content.append(fc)
	content.append(ec)
	content.append(date)
	if sentence in sentence_dictionary:
		return sentence_dictionary
	else:
		sentence_dictionary[sentence] = content 
		return sentence_dictionary


def getSentence(line):
	index1=line.find('b')

	line = line[index1+2:]
	index2 =line.find('\"')
	if index2 == -1:
		index2 = line.find('\'')

	sentence = line[:index2-1]

	
	#print(sentence)
	return sentence

def remove(sentence):
	#remove dollar sign

	sentence = sentence.split(" ")
	newsentence = ''
	for words in sentence:
		result = re.match(r"\s*\$\w+",words)
		if result == None:
			if newsentence == '':
				newsentence = words 
			else:
				newsentence = newsentence + ' ' + words 
		else:
			continue
	#print(newsentence)

	#remove https://
	sentence = newsentence
	newsentence = ''
	sentence = sentence.split(" ")
	for words in sentence:
		result = re.findall(r"(\s*https://\w*.\w*)",words)
		if len(result) == 0:
			if newsentence == '':
				newsentence = words 
			else:
				newsentence = newsentence + ' ' + words	 
		else:
			continue
	#print(newsentence)	 

	#remove RT
	sentence = newsentence
	newsentence = ''
	sentence = sentence.split(" ")
	for words in sentence:
		result = re.findall(r"RT\s*",words)
		if len(result) == 0:
			if newsentence == '':
				newsentence = words 
			else:
				newsentence = newsentence + ' ' + words	 
		else:
			continue
	
	sentence = newsentence
	newsentence = ''
	sentence = sentence.split(" ")
	if len(sentence) >= 5:
		for words in sentence:
			if words == '':
				continue
			else:
				words=words.replace('\'','')
				words=words.replace('!','')
				words=words.replace('?','')
				words=words.replace('%','')
				words=words.replace(',','')
				words=words.replace(')','')
				words=words.replace('(','')
				words=words.replace(';','')
				words=words.replace(':','')	
				words=words.replace('\\n','')
				words=words.replace('-','')
				words=words.replace('.','')
				words=words.replace('|','')
				words=words.replace('#','')
				words=words.replace('$','')
				words=words.replace('&amp','')
				words=words.replace('+','')
				words=words.replace('&lt',' ')
				words=words.replace('&gt',' ')
				result = re.findall(r"@\w*\s*",words)
				if len(result) == 0:
					if newsentence == '':
						newsentence = words 
					else:
						newsentence = newsentence + ' ' + words	 
				else:
					continue
	newsentence = newsentence.lower()
	#print(newsentence)
	return newsentence
	 
	
def readFile(filename):
	rf = open('./dataset/'+filename,'r')
	sentence_dictionary = dict()
	count = 0
	date,company=filename.split('$')
	#print(date,company)
	
	for line in rf:
		line = line[:-1]
		msg=getSentence(line)
		engage_count = (line[-1]) #engage
		favorite_count = (line[-3]) #favorite
		retweet_count = (line[-5]) #retweet

		if len(msg) <=4:
			continue
		
	
		msg=remove(msg)
		sentence_dictionary = checkDuplicate(msg,retweet_count,favorite_count,engage_count,date)
		#print(sentence_dictionary)

	#print(len(sentence_dictionary))
	return sentence_dictionary	
	