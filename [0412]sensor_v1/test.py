# -*- coding:utf-8 -*-
import sys
import time
import requests
import json



def waitingforchange():



	print ("기저귀 교체완료")

	url = "http://localhost:8080/smartDiaper/change"
	data =  {'sid': 'SmartDiaper-1', 'signal': 'change'}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	res = requests.post(url, data=json.dumps(data), headers=headers)

	print (res)

	time.sleep(2)






print ("기저귀를 교체해주세요!")

url = "http://localhost:8080/smartDiaper/sensing"
data =  {'sid': 'SmartDiaper-1', 'signal': 'sensing'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
res = requests.post(url, data=json.dumps(data), headers=headers)

print (res)

time.sleep(2)

waitingforchange()
