import filter
import sys
import os
from multiprocessing import Pool

processes = ('fetchtweets.py $AAPL','fetchtweets.py $GOOG','fetchtweets.py $AMZN','fetchtweets.py $TSLA','fetchtweets.py $MSFT','fetchtweets.py $NFLX','fetchtweets.py $BBRY','fetchtweets.py $JCP','fetchtweets.py $FB','fetchtweets.py $VRNG')

def run_process(process):
	os.system('python {}'.format(process))


if __name__ == '__main__':
	pool = Pool(processes=10)
	pool.map(run_process,processes)


#filter.cleaningFile()
