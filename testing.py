import filter
import os

#filter.readFile('2018-07-26$AAPL')

files = os.listdir('./dataset/')
for file in files:
	filter.readFile(file)