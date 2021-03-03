from iota import Iota
from iota import ProposedTransaction
from iota import Address
from iota import Tag
from iota import TryteString
import sys
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']
# returns JSON object as  
# a dictionary 
api = Iota(url, testnet = True) 
address = 'ZLGVEQ9JUZZWCZXLWVNTHBDX9G9KZTJP9VEERIIFHY9SIQKYBVAHIMLHXPQVE9IXFDDXNHQINXJDRPFDXNYVAPLZAW'
message = TryteString.from_unicode('Hello world')

tx = ProposedTransaction(
address = Address(address),
message = message,
value = 0
)

num = 1
if len(sys.argv) == 2:
    num = int(sys.argv[1])

for i in range(num):
    result = api.send_transfer(transfers = [tx])
    print(result['bundle'].tail_transaction.hash)