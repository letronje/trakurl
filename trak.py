#! /usr/bin/python

import urllib
import base64
from sys import argv, exit

if len(argv) < 2:
	print "Missing Url"
	exit()

url = argv[1]

API_HOST = "trakurl.appspot.com"
#API_HOST = "localhost:8080"
api_url =  "http://" + API_HOST + "/create?b64url="+base64.b64encode(url)

print "http://" + API_HOST + "/goto?" + urllib.urlopen(api_url).read()
