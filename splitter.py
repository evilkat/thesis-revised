import sys

fil = sys.argv[1]
csvfilename = open(fil,'r').readlines()
file = 1
for j in range(len(csvfilename)):
	if j%100000 == 0:
		open(str(fil)+str(fil)+'.csv','w+').writelines(csv[j:j+100000])
		file += 1