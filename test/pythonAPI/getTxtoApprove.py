import urllib.request as urllib2
import json

def getTxToApprove():
    with open('config.json', 'r') as f:
        data = json.load(f)
        url = data['url']

    command = {
    "command": "getTransactionsToApprove"
    }

    stringified = json.dumps(command).encode("utf-8")

    headers = {
        'content-type': 'application/json',
        'X-IOTA-API-Version': '1'
    }

    request = urllib2.Request(url=url, data=stringified, headers=headers)
    returnData = urllib2.urlopen(request).read()

    jsonData = json.loads(returnData)
    return jsonData
    
print(getTxToApprove())