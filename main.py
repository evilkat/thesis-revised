import filter
import sys
import os
from multiprocessing import Pool

#list of the processes to be executed
processes = ('fetchtweets.py $AAPL','fetchtweets.py $GOOG','fetchtweets.py $AMZN','fetchtweets.py $TSLA','fetchtweets.py $MSFT','fetchtweets.py $NFLX','fetchtweets.py $BBRY','fetchtweets.py $JCP','fetchtweets.py $FB','fetchtweets.py $VRNG')

#calling of the scripts
def run_process(process):
	os.system('python {}'.format(process))

#putting the processes in a pool
if __name__ == '__main__':
	pool = Pool(processes=10)
	pool.map(run_process,processes)


#filter.cleaningFile()
