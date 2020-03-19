#!/usr/bin/env python
import time
import sys
import pyjulius
import Queue
import urllib2
import os
import subprocess

# score threshold value, words with smaller score will be discarded
threshold = 70
client = pyjulius.Client('localhost', 10500)

try:
	print "Starting julius..."
	FNULL = open(os.devnull, 'w')
	subprocess.Popen(["julius/julius/julius", "-C", "settings.jconf", "-dnnconf", "dnn.jconf"], stdout=FNULL, stderr=FNULL)
except:
	Stopped
	sys.exit();
print "Done."

while 1:
	try:
		client.connect()
		print "Connected. Ready for user input."
		break
	except pyjulius.ConnectionError:
		print "Waiting for julius to fully start up..."
		try:
			time.sleep(1)
		except KeyboardInterrupt:
			print "Stopped."
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
				print "Word: %s\tScore: %.2f" % (result, result.score)
				if str(result) == "lumos":
					try:
						urllib2.urlopen("http://lumen.local/?state=on")
					except:
						pass
				elif str(result) == "nox":
					try:
						urllib2.urlopen("http://lumen.local/?state=off")
					except:
						pass
			else:
				print "Discarded.\tScore: %.2f" % (result.score)

# handle user interrupt
except KeyboardInterrupt:
	print "Stopped."
# cleanup
finally:
	client.stop()
	client.join()
	client.disconnect()
