#!/usr/bin/python

from AppKit import CWInterface
import socket
import time
from urllib2 import urlopen, URLError, HTTPError

starttime=time.time()

def reConnect():
	iface = CWInterface.interface()
	iface.setPower_error_(False, None)
	iface.setPower_error_(True, None)

	print "your wifi should work now!"

def wifiCorrect():
	socket.setdefaulttimeout( 0.2 )

	url = 'http://google.com/'
	try :
		response = urlopen( url )
	except HTTPError, e:
		print 'The server couldn\'t fulfill the request. Reason:', str(e.code)
	except URLError, e:
		print 'We failed to reach a server. Reason:', str(e.reason)
		reConnect()
	except socket.timeout as e:
		reConnect()
	else :
		print 'got response!'

while True:
	wifiCorrect()
	time.sleep(10.0 - ((time.time() - starttime) % 10.0))