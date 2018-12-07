import pandas as pd
import numpy as np


#listdate = ['2018-07-26','2018-07-27','2018-07-30','2018-08-01','2018-08-02','2018-08-06','2018-08-07','2018-08-08','2018-08-09','2018-08-10','2018-08-13','2018-08-14','2018-08-15','2018-08-20','2018-08-23','2018-08-28','2018-08-30']
#listdate = ['2018-09-03','2018-09-04','2018-09-05','2018-09-06','2018-09-07','2018-09-10','2018-09-11','2018-09-12','2018-09-13','2018-09-17','2018-09-18','2018-09-19','2018-09-20','2018-09-21','2018-09-24','2018-09-25','2018-09-26','2018-09-27','2018-09-29',]
#listdate = ['2018-10-01','2018-10-02','2018-10-03','2018-10-04','2018-10-05','2018-10-08','2018-10-09','2018-10-10','2018-10-11','2018-10-12','2018-10-15','2018-10-16','2018-10-17','2018-10-18','2018-10-19','2018-10-22','2018-10-23','2018-10-24','2018-10-29','2018-10-30',]
#listdate = ['2018-11-05','2018-11-06','2018-11-13','2018-11-14','2018-11-15','2018-11-19','2018-11-21']
for date in listdate:
	try:
		data = pd.read_csv('withsentiment/AAPL'+date+'.csv',sep=',')
		print(date,data['sentiment'].mean(),len(data['sentiment']))
		neg_value = data['sentiment'] < 0
		pos_value = data['sentiment'] > 0
		print('negative: ' + str(len(data[neg_value])))
		print('positive: ' + str(len(data[pos_value])))
		#print(neg_value)
		#print(len(neg_value))
		#print(len(pos_value))
	except BaseException as e:
		print(e)