#////////////////////////////////////////////////
#// Send a microtransaction
#////////////////////////////////////////////////

from iota import Iota
from iota import ProposedTransaction
from iota import Address

import json

with open('config.json', 'r') as f:
    data = json.load(f)
    url = data['url']
# Replace this seed with the one that owns the address you used to get free test tokens
seed = 'QUOORPDGVAOPTZLJ9VENMYVJHUYG9IGBHGTFBPMMOLMB9QFEDDLSXQTBYLTLWCYBDUKDFPJZDERXYCLXA'
input_addr = Address('PYJNIVWXVDPEZMRWFKMCHXHDESECFXYASQDNYGKQZWBHR99POMPULDSVQGRFOYAPCGMKCHDWWFCOYZAEA')
# Connect to a node
api = Iota(url, seed, testnet = True)

# Define an address to which to send IOTA tokens 
address = 'B9WSEPNPHMEIWIAUQIKUVBGKSBTIVZHFKDNWAVNWTRQUKBUWBE9VUME9DGFEHVAWNJZMEBNCOURPHYDAB'

# Define an input transaction object
# that sends 1 i to the address
tx = ProposedTransaction(
    address=Address(address),
    value = 10000
)

print('Sending 10000 i to ',  address)

result = api.send_transfer(transfers=[tx],inputs=[[input_addr]] )

print('Bundle: ')
print(result['bundle'].hash)

