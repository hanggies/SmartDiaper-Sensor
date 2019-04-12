# -*- coding:utf-8 -*-
import sys
import time
import os
import requests
import json



def waitingforchange():

	myhost = os.uname()[1]

	print "기저귀 교체완료"

	url = "http://192.168.0.5:8080/smartDiaper/change"
	data =  {'sid': myhost, 'signal': 'change'}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	res = requests.post(url, data=json.dumps(data), headers=headers)

	print res

	time.sleep(2)


myhost = os.uname()[1]

print myhost

print "기저귀를 교체해주세요!"

url = "http://192.168.0.5:8080/smartDiaper/sensing"
data =  {'sid': myhost, 'signal': 'sensing'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res = requests.post(url, data=json.dumps(data), headers=headers)

print res

time.sleep(2)

waitingforchange()
