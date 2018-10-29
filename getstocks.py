from pandas_datareader import data as pdr
import fix_yahoo_finance as yf

yf.pdr_override()

def printDataInfile(dat,symbol):

	if len(data.keys()) != 0:
		print(data.keys())
		wr = open("stocks/stockprices$"+symbol+".txt","a")
		wr.write(str(data))
		wr.close()

ticker_symbol = ["AAPL","TSLA","BBRY","FB","GOOG","MSFT","JCP","VRNG","AMZN","NFLX"]

for i in ticker_symbol:
	data = pdr.get_data_yahoo(tickers=i,start="2018-07-25",as_panel=False,group_by='ticker',actions=True,thread=10)
	print(data)
	printDataInfile(data,i)
