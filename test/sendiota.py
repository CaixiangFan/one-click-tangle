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
seed = 'QTPTQCDVTAPWRFOVHKLHUEAYETHLQZCN9WHMM9P99GKLOLADGTTMAGNNYROSOOBWLOJONWLWMBWCDIYPD'

# Connect to a node
api = Iota(url, seed, testnet = True)

# Define an address to which to send IOTA tokens 
address = 'B9WSEPNPHMEIWIAUQIKUVBGKSBTIVZHFKDNWAVNWTRQUKBUWBE9VUME9DGFEHVAWNJZMEBNCOURPHYDAB'

# Define an input transaction object
# that sends 1 i to the address
tx = ProposedTransaction(
    address=Address(address),
    value = 1
)

print('Sending 1 i to ',  address)

result = api.send_transfer(transfers=[tx] )

print('Bundle: ')
print(result['bundle'].hash)

