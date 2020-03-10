#!/usr/bin/env python
import time
import sys
import pyjulius
import Queue

# score threshold value, words with smaller score will be discarded
threshold = 70
client = pyjulius.Client('localhost', 10500)

# startup delay for julius to finish setup
time.sleep(5)
try:
	client.connect()
	print "Connected. Ready for user input."
except pyjulius.ConnectionError:
	print "Error: Start julius as module first."
	sys.exit(1)

# main loop
client.start()
try:
	while 1:
		try: 
			result = client.results.get(False)
		except Queue.Empty:
			continue
		if isinstance(result, pyjulius.Sentence):
			if (result.score >= threshold):
				print "Word: %s\t Score: %.2f" % (result, result.score)
			else:
				print "Discarded. Score: %.2f" % (result.score)

# handle user interrupt
except KeyboardInterrupt:
	print "Stopped."
# cleanup
finally:
	client.stop()
	client.join()
	client.disconnect()
