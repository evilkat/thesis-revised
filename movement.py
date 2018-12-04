import os

def fileReader(file):
	fp = open(file,"r")

	stockvalues = list()
	cnt = 0
	for line in fp:
		if cnt == 0:
			cnt = cnt + 1
			continue
		else:
			line = line[:-1]
			line = line.split(",")
			stockvalues.append(line)
	fp.close()
	return stockvalues
def writeFile(file,stockvalues):
	fp = open(file,"a")
	print(stockvalues)
	
	for i in range(0,len(stockvalues)):
		if float(stockvalues[i][-2]) - float(stockvalues[i][1]) < 0:
			fp.write(stockvalues[i][0]+','+stockvalues[i][1] + ','+ stockvalues[i][2] + ',' + stockvalues[i][3] +',' + stockvalues[i][4] + ',' +stockvalues[i][5] + ','+stockvalues[i][6]+','+'-1'+'\n')
			print("Negative")
		elif float(stockvalues[i][-2]) - float(stockvalues[i][1]) > 0:
			fp.write(stockvalues[i][0]+','+stockvalues[i][1] + ','+ stockvalues[i][2] + ',' + stockvalues[i][3] +',' + stockvalues[i][4] + ',' +stockvalues[i][5] + ','+stockvalues[i][6]+','+'1'+'\n')
			print("Positive")
		else:
			fp.write(stockvalues[i][0]+','+stockvalues[i][1] + ','+ stockvalues[i][2] + ',' + stockvalues[i][3] +',' + stockvalues[i][4] + ',' +stockvalues[i][5] + ','+stockvalues[i][6]+','+'0'+'\n')
			print("Neutral")
	fp.close()


files = os.listdir('./stocks/')
for file in files:
	filename,extension = file.split(".")
	stockvalues = list()
	stockvalues=fileReader('stocks/'+file)
	writeFile('stocks/'+filename+'movement.csv',stockvalues)