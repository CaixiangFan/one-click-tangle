import urllib.request as urllib2
import json
import sys
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']

address = "B9OOTDUXTUSQZRU9TPHPHYRCUPUWBJFFFJQCFYZELFTGDGDTKFVMXXAKY9JOIEJ9VDCZYEGS9GXCFVHCA"

if len(sys.argv) == 2:
    address = sys.argv[1]

command = {
  "command": "getBalances",
  "addresses": [
    address
  ]
}

stringified = json.dumps(command).encode("utf-8")

headers = {
    'content-type': 'application/json',
    'X-IOTA-API-Version': '1'
}

request = urllib2.Request(url=url, data=stringified, headers=headers)
returnData = urllib2.urlopen(request).read()

jsonData = json.loads(returnData)

print(jsonData)