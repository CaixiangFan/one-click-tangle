import urllib.request as urllib2
import json
import getTxtoApprove

tipData = getTxtoApprove.getTxToApprove()

command = { 
"command": "attachToTangle", 
"trunkTransaction": tipData['trunkTransaction'],
"branchTransaction": tipData['branchTransaction'],
"trytes": [
  "HOHZUBAFSGNYMOOYGPCKANKOR ...",
  "IOELDJYWAZBKWBTQZYLPTPLIT ..."
  ]
}

stringified = json.dumps(command).encode("utf-8")

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

request = urllib2.Request(url=url, data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)

print(jsonData)