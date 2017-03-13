from urllib.request import urlopen
import time
import datetime

stocksToPull = 'AAPL', 'GOOG', 'GPRO', 'AMZN', 'EBAY', 'TSLA', 'MSFT'

def pullData(stock):
	try:
		print('Currently pulling', stock)
		print(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
		urlToVisit = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=1d/csv'
		saveFileLine = stock + '.txt'

		try:
			readExistingData = open(saveFileLine, 'r').read()
			splitExisting = readExistingData.split('\n')
			mostRecentLine = splitExisting[-2]
			lastUnix = int(mostRecentLine.split(',')[0])

		except Exception as e:
			print(str(e))
			time.sleep(1)
			lastUnix = 0

		saveFile = open(saveFileLine, 'a')
		sourceCode = urlopen(urlToVisit).read().decode('utf-8')
		splitSource = sourceCode.split('\n')

		for eachLine in splitSource:
			if 'values' not in eachLine:
				splitLine = eachLine.split(',')

				if len(splitLine) == 6:

				
					if int(splitLine[0]) > int(lastUnix):
						lineToWrite = eachLine + '\n'
						saveFile.write(lineToWrite)
		saveFile.close()

		print('Pulled', stock)
		print('Sleeping')
		print(str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
		time.sleep(1)



	except Exception as e:
		print('main loop', str(e))

while True:
	for eachStock in stocksToPull:
		pullData(eachStock)