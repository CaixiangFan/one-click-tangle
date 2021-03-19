import urllib.request as urllib2
from iota import Address, TryteString, TransactionTrytes
import json, sys

command_ts = {
    "command": "getTransactionsToApprove"
}
stringified_ts = json.dumps(command_ts).encode("utf-8")
headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

request_ts = urllib2.Request(url=url, data=stringified_ts, headers=headers)
jsonData = json.loads(urllib2.urlopen(request_ts).read())

# propose a transaction and input trytes string to "trytes"
address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
message = TryteString.from_unicode('Hello world')

trytes = TransactionTrytes(message)
command_pow = { 
    "command": "attachToTangle", 
    "trunkTransaction": jsonData['trunkTransaction'],
    "branchTransaction": jsonData['branchTransaction'],
    "trytes": [str(trytes)]
}
stringified_pow = json.dumps(command_pow).encode("utf-8")
request_pow = urllib2.Request(url=url, data=stringified_pow, headers=headers)
returnData = urllib2.urlopen(request_pow).read()
jsonData_pow = json.loads(returnData)
print(jsonData_pow['trytes'])